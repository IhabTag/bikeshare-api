import time
import pandas as pd
import numpy as np
import data

def df_city(city):
    city = city + ".csv"
    filename = pd.read_csv(city)
    df = pd.DataFrame(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + " to " + df['End Station']

    return df

def df_months(df_city, months):
    df_months = pd.DataFrame()
    for month in months:
        df_selected_month = df_city[df_city['month'] == month]
        df_months = df_months.append(df_selected_month, ignore_index = True)
    return df_months

def df_days(df_months, days):
    df_days = pd.DataFrame()
    for day in days:
        df_selected_day = df_months[df_months['week day'] == day]
        df_days = df_days.append(df_selected_day)
    return df_days

def time_stats(df):

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

    # Display counts of user types

    subscribers_count = df['User Type'].value_counts()[0]
    customers_count = df['User Type'].value_counts()[1]

    # Display counts of gender
    
    males_count = df['Gender'].value_counts()[0]
    females_count = df['Gender'].value_counts()[1]

    # Display earliest, most recent, and most common year of birth
    
    min_db_year = int(df['Birth Year'].min())
    max_db_year = int(df['Birth Year'].max())
    mode_db_year = int(df['Birth Year'].mode()[0])

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

def execute_analysis(city, months, days):
    
    my_df_city = df_city(city)
    my_df_months = df_months(my_df_city, months)
    my_df_day = df_days(my_df_months, days)

    my_time_stats          = time_stats(my_df_day)
    my_station_stats       = station_stats(my_df_day)
    my_trip_duration_stats = trip_duration_stats(my_df_day)
    my_user_stats          = user_stats(my_df_day)
    return [my_time_stats, my_station_stats, my_trip_duration_stats, my_user_stats]
