import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAYS_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York or Washington?\n')
            if city and city.lower() in CITY_DATA:
                break
            else:
                print('\nPlease type a valid city name!')
        except (KeyboardInterrupt):
            print('Good bye!')
            break
        except:
            print('Something went wrong, please try again')

    # get user input for month (all, january, february, ... , june)
    month = ""
    months_dict = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "all": 7}
    while True:
        try:
            month = input('Which month? January, February, March, April, May or June? Please type out the full month name or type "all" to get all months.\n')
            if month and month.lower() in months_dict:
                break
            else:
                print('Please type a valid month name!\n')
        except (KeyboardInterrupt):
            print('Good bye!')
            break
        except:
            print('Something went wrong, please try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while True:
        try:
            day = input('Which day?\n')
            if day.lower() in DAYS_LIST:
                break
            else:
                print('Please type a valid day (e.g., Monday, Tuesday...).\n')
        except (KeyboardInterrupt):
            print('Good bye!')
            break
        except:
            print('Something went wrong, please try again')

    print('-'*40)
    return CITY_DATA[city.lower()], months_dict[month.lower()], day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = pd.read_csv(city)
    df = pd.DataFrame(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    # return df
    if month and day:
        return df.loc[(df['month'] == month) & (df['week day'] == DAYS_LIST.index(day.lower()))]
    elif month and not day:
        return df['month'] == month
    elif day:
        return df['week day'] == DAYS_LIST.index(day.lower())

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months_list = ["January", "February", "March", "April", "May", "June"]
    print('The most common month is: {}\n'.format(months_list[df['month'].mode()[0]-1]))

    # display the most common day of week
    print('The most common day of the week is: {}\n'.format(DAYS_LIST[df['week day'].mode()[0]]))

    # display the most common start hour
    print('The most common hour is: {}\n'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: {}\n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most common end station is: {}\n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most common trip is : from {}\n'.format(df['trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is : {}\n'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Mean travel time is : {}\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of "Subscriber" user type is: {}\nCount of "Customer" user type is: {}'
    .format(df['User Type'].value_counts()[0], df['User Type'].value_counts()[1]))

    # Display counts of gender
    print('Count of "Male" users is: {}\nCount of "Female" users is: {}'
    .format(df['Gender'].value_counts()[0], df['Gender'].value_counts()[1]))

    # Display earliest, most recent, and most common year of birth
    print('Earliest date of birth is: {}\nMost recent date of birth is: {}\nMost common year of birth is: {}'
    .format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # df_sliced = df[['Trip Duration']]
        # print(df.head())
        # print(df_sliced.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
