import time
import pandas as pd
import numpy as np
import data

def df_city(city):
    '''
        Returns the dataframe of the selected city

            Parameters:
                city (str): The city name as a string
            
            Returns:
                Pandas DataFrame (object): Dataframe object of the selected city data
    '''

    city = city + ".csv"
    filename = pd.read_csv(city)
    df = pd.DataFrame(filename)
    df['Start Timestamp'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Timestamp'].dt.month
    df['week day'] = df['Start Timestamp'].dt.dayofweek
    df['hour'] = df['Start Timestamp'].dt.hour
    df['trip'] = df['Start Station'] + " to " + df['End Station']

    return df

def df_months(df_city, months):
    '''
        Returns the dataframe of the selected month

            Parameters:
                df_city (obj)   : The dataframe of the selected city as a Pandas dataframe object
                months (array)  : The selected months as array of strings
            
            Returns:
                Pandas DataFrame (object): Dataframe object of the selected city data filtered by selected months
    '''

    df_months = pd.DataFrame()
    for month in months:
        df_selected_month = df_city[df_city['month'] == month]
        df_months = df_months.append(df_selected_month, ignore_index = True)
    return df_months

def df_days(df_months, days):
    '''
        Returns the dataframe of the selected days

            Parameters:
                df_months (obj) : The dataframe of the selected city filtered by selected months as a Pandas dataframe object
                days (array)    : The selected days as array of strings
            
            Returns:
                Pandas DataFrame (object): Dataframe object of the selected city data filtered by selected months and selected days
    '''

    df_days = pd.DataFrame()
    for day in days:
        df_selected_day = df_months[df_months['week day'] == day]
        df_days = df_days.append(df_selected_day, ignore_index = True)
    return df_days

def time_stats(df):
    '''
        Returns the a dictionary with the specified statistics

            Parameters:
                df (obj) : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
            
            Returns:
                A dictionary of the specified statistics
    '''

    # display the most common month
    mode_month = df['month'].mode()[0]

    # display the most common day of week
    mode_day = df['week day'].mode()[0]

    # display the most common start hour
    mode_hour = df['hour'].mode()[0]

    stats = {
        "month": int(mode_month),
        "day"  : int(mode_day),
        "hour" : int(mode_hour)
    }

    return stats

def station_stats(df):
    '''
        Returns the a dictionary with the specified statistics

            Parameters:
                df (obj) : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
            
            Returns:
                A dictionary of the specified statistics
    '''

    # display most commonly used start station
    mode_start = df['Start Station'].mode()[0]

    # display most commonly used end station
    mode_end = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    mode_trip = df['trip'].mode()[0]

    stats = {
        "start": mode_start,
        "end"  : mode_end,
        "trip" : mode_trip
    }

    return stats

def trip_duration_stats(df):
    '''
        Returns the a dictionary with the specified statistics

            Parameters:
                df (obj) : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
            
            Returns:
                A dictionary of the specified statistics
    '''
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    stats = {
        "total" : int(total_travel_time),
        "mean"  : int(mean_travel_time)
    }
    return stats

def user_stats(df):
    '''
        Returns the a dictionary with the specified statistics

            Parameters:
                df (obj) : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
            
            Returns:
                A dictionary of the specified statistics
    '''
    # Display counts of user types
    subscribers_count = df['User Type'].value_counts()[0]
    customers_count = df['User Type'].value_counts()[1]

    # Display counts of gender
    males_count = df['Gender'].value_counts()[0] if 'Gender' in df.columns else 0
    females_count = df['Gender'].value_counts()[1] if 'Gender' in df.columns else 0

    # Display earliest, most recent, and most common year of birth  
    min_db_year = int(df['Birth Year'].min()) if 'Birth Year' in df.columns else 0
    max_db_year = int(df['Birth Year'].max()) if 'Birth Year' in df.columns else 0
    mode_db_year = int(df['Birth Year'].mode()[0]) if 'Birth Year' in df.columns else 0

    stats = {
        "subscriber" : int(subscribers_count),
        "customer"    : int(customers_count),
        "male"       : int(males_count),
        "female"     : int(females_count),
        "min"       : (min_db_year),
        "max"       : max_db_year,
        "mode"      : mode_db_year
    }

    return stats

def get_df(city, months, days):
    '''
        Loading the dataframe of the specified city and applying months and days filters to return the required dataframe

            Parameters:
                city (str)      : The city name as a string
                months (array)  : The selected months as array of strings
                days (array)    : The selected days as array of strings
            
            Returns:
                Pandas DataFrame (object): Dataframe object of the selected city data filtered by selected months and selected days
    '''

    my_df_city = df_city(city)
    my_df_months = df_months(my_df_city, months)
    my_df_days = df_days(my_df_months, days)
    return my_df_days

def execute_analysis(df):
    '''
        Loading the specified dataframe and applying statistics calculation functions

            Parameters:
                df (obj) : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
            
            Returns:
                Array (object): Array of calculated statistics as objects
    '''

    my_time_stats          = time_stats(df)
    my_station_stats       = station_stats(df)
    my_trip_duration_stats = trip_duration_stats(df)
    my_user_stats          = user_stats(df)
    return [my_time_stats, my_station_stats, my_trip_duration_stats, my_user_stats]

def get_users(df, start=0, end=5):
    '''
        Function to slice a dataframe

            Parameters:
                df (obj)    : The dataframe of the selected city filtered by selected months and days as a Pandas dataframe object
                start (int) : The start index of the original dataframe to slice from (inclusive) - default = 0
                end (int)   : The enf index of the original dataframe to slice to (exclusive) - default = 5
            
            Returns:
                Pandas DataFrame (object): Dataframe object of the selected city data filtered by selected months and selected days
                                           that contains only 5 rows
    '''

    sliced_df = df[start : end]
    return sliced_df
