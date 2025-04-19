"""
Importing necessary libraries:
- time: for time-related functions (e.g., pauses or tracking execution time)
- pandas (pd): for data manipulation and analysis using DataFrames
- numpy (np): for numerical operations and efficient array handling
"""

import time
import pandas as pd
import numpy as np

# Lists
VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
VALID_DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("\nGive us a city: ").lower()
        if city in VALID_CITIES:
            break
        else:
            print("\nPlease type 'Chicago', 'New York City' or 'Washington'")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("\nGive us a month: ").lower()
        if month in VALID_MONTHS:
            break
        else:
            print("\nPlease select a valid month or 'all'")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("\nGive us a day of the week: ").title()
        if day in VALID_DAYS:
            break
        else:
            print("\nPlease select a valid day of the week or 'all'")

    print('\n')
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
    
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    if month != 'all':
        print("You're seeing stats for the month of {}".format(month))
    else:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = df['month'].mode()[0]  # Most common month as a number
        print("The most popular month for a ride is {}".format(months[popular_month - 1]))

    # TO DO: display the most common day of week
    if ((day == 'All') and (month == 'all')):
        popular_day = df['day_of_week'].mode()[0]
        print("\nThe most popular day for a ride is {}".format(popular_day))
    elif day == 'All':
        print("\nNow let's look at stats for all days in {}".format(month))
    elif month == 'all':
        print("\nNow, let's look at stats for {}s in {}".format(day, months[popular_month - 1]))
    else:
        print("As selected, let's look at stats for {}s in {}".format(day, month))

    # TO DO: display the most common start hour
    print("\nAnd the most popular time for a ride is {}\n".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    
    print('-'*40)

def station_stats(df):
            
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start and end stations
    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    if popular_start_station == popular_end_station:
        print("The most commonly used start and end station is {}".format(df['Start Station'].mode()[0]))
    else:
        print("The most commonly used start station is {}".format(df['Start Station'].mode()[0]))
        print("\nThe most commonly used end station is {}\n".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trips'] = "starts at " + df['Start Station'] + " and ends at " + df['End Station']
    print("\nThe most common trip {}\n".format(df['trips'].mode()[0]))

    print("This took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()

    days = int(total_duration // 86400)
    hours = int((total_duration % 86400) // 3600)
    minutes = int(((total_duration % 86400) % 3600) // 60)
    
    avg_minutes = int(mean_duration // 60)
    avg_seconds = int(mean_duration % 60)
    
    # TO DO: display total travel time
    print(f"Total travel time is {days} days, {hours} hours, and {minutes} minutes\n")

    # TO DO: display mean travel time
    print(f"And the average travel time is {avg_minutes} mins and {avg_seconds} seconds")

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
            
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("See below the counts of user types:\n")
    for index, value in df['User Type'].value_counts().items():
        print(index, value)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nAnd the number of male and female users:\n")
        for index, value in df['Gender'].value_counts().items():
            print(index, value)
    else:
        print("\nNo gender data available for this city\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nThe oldest user was born in", int(df['Birth Year'].min()),"\n")
        print("And the youngest one in", int(df['Birth Year'].max()), "\n")
        print("The most common year of birth in our dataset is", int(df['Birth Year'].mode()[0]))
    else:
        print("No birth year data available")


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data if the user wants to"""
    x = 0
    while True:
        raw_data = input("\nDo you want to see 5 rows of raw data? ").lower()
        if raw_data == 'yes':
            print("\n",df[x:x+5])
            x = x + 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()