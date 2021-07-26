import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    CITY_LIST = ['chicago', 'new york city', 'washington']

    print("\nPlease choose a city.")
    print("\nAccepted input: 'chicago', 'new york city', 'washington'")

    CITY_INPUT = input().lower()

    while CITY_INPUT not in CITY_LIST:
        print('\nSorry, no data found. Please check the available options and the format of your input.')
        CITY_INPUT = input().lower()

    city = CITY_INPUT


    # TO DO: get user input for month (all, january, february, ... , june)

    MONTH_LIST = ['january', 'february', 'march', 'april', 'june', 'all']

    print("\nPlease choose a month.")
    print("\nAccepted input: 'january', 'february', 'march', 'april', 'june', 'all'.")

    MONTH_INPUT = input().lower()

    while MONTH_INPUT not in MONTH_LIST:
        print('\nSorry, no data found. Please check the available options and the format of your input.')
        MONTH_INPUT = input().lower()

    month = MONTH_INPUT


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    DAY_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    print("\nPlease choose a weekday.")
    print("\nAccepted input: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'")

    DAY_INPUT = input().lower()

    while DAY_INPUT not in DAY_LIST:
        print('\nSorry, no data found. Please check the available options and the format of your input.')
        DAY_INPUT = input().lower()

    day = DAY_INPUT


    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def Time_Stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]

    print('Most Popular Month (1 = January etc.):', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print('Most Popular Day of Week:', popular_day)


    # TO DO: display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Station_Stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Journey'] = df['Start Station'].str.cat(df['End Station'], sep=' -> ')
    most_frequent_journey = df['Journey'].mode()[0]

    print('Most frequent journey:', most_frequent_journey)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Trip_Duration_Stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time_seconds = df['Trip Duration'].sum()
    total_travel_time_minutes = total_travel_time_seconds / 60
    total_travel_time_hours = total_travel_time_minutes / 60

    print('Total travel time in seconds:', total_travel_time_seconds)
    print('Total travel time in minutes:', total_travel_time_minutes)
    print('Total travel time in hours:', total_travel_time_hours)

    # TO DO: display mean travel time

    mean_travel_time_seconds = df['Trip Duration'].mean()
    mean_travel_time_minutes = mean_travel_time_seconds / 60
    mean_travel_time_hours = mean_travel_time_minutes / 60

    print('\nMean travel time in seconds:', mean_travel_time_seconds)
    print('Mean travel time in minutes:', mean_travel_time_minutes)
    print('Mean travel time in hours:', mean_travel_time_hours)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def User_Stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # TO DO: Display counts of gender

    try:
        gender = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender)

    except:
        print("\nSorry, no data found for 'Gender' in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year = int(df['Birth Year'].min())
        latest_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print('\nEarliest year of birth:', earliest_year)
        print('Latest year of birth:', latest_year)
        print('Most common year of birth:', most_common_year)

    except:
        print("\nSorry, no data found for 'Birth Year' in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Display_Data(df):
    """Displays raw data upon request."""

    start_time = time.time()

    VIEW_DATA = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    RESPONSE_LIST = ['yes', 'no']
    start_loc = 0

    while True:
        if VIEW_DATA not in RESPONSE_LIST:
           VIEW_DATA = input('\nInvalid input. Please enter yes or no.\n').lower()
        elif VIEW_DATA == 'yes':
            start_loc += 5
            print(df.iloc[start_loc : start_loc + 5])
            REPEAT = input('\nWould you like to view 5 more rows? Enter yes or no.\n').lower()
            if REPEAT not in RESPONSE_LIST:
                VIEW_DATA = input('\nInvalid input. Please enter yes or no.\n').lower()
            elif REPEAT == 'no':
                break
        elif VIEW_DATA == 'no':
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        Display_Data(df)
        Time_Stats(df)
        Station_Stats(df)
        Trip_Duration_Stats(df)
        User_Stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
