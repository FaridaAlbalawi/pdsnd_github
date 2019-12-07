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
    city=input('Choose a city:  chicago, new york city, washington \n').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('invalid input,please try again ')
        city=input('Choose a city:  chicago, new york city, washington \n').lower()
         


    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Choose a month:  all, january, february, ... , june \n').lower()
    while month not in ('all','january', 'february', 'march','april', 'may', 'june'):
        print('invalid input,please try again ')
        month=input('Choose a month:  all, january, february, ... , june \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Choose a day:  all, monday, tuesday, ... sunday \n').lower()
    while day not in ('all','monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday'):
         print('invalid input,please try again ')
         day=input('Choose a day:  all, monday, tuesday, ... sunday \n').lower()

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
       
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print ('Most Frequent Month: ',popular_month)

    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('Most Frequent Day of week:', popular_dayofweek)
 

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ('Most Frequent Start Station: ',popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ('Most Frequent End Station: ',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combination'] = df['Start Station'].str.cat(df['End Station'], sep =" TO ") 
    start_end_combination = df['start_end_combination'].mode()[0]
    print ('most frequent combination of start station and end station trip: FROM ',start_end_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration=df['Trip Duration'].sum()
    print('total trip duration: {} seconds '.format(trip_duration))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types: ',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('counts of gender: ',user_gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if  'Birth Year' in df:   
       popular_birth_year= df['Birth Year'].mode()[0] 
       print ('most frequent year of birth: ',popular_birth_year)
       earliest_birth_year= df['Birth Year'].min()
       print ('earliest year of birth: ',earliest_birth_year)
       recent_birth_year= df['Birth Year'].max()  
       print ('most recent year of birth: ',recent_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def main():
    while True:
        user=input('enter your name: \n').capitalize()
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        want_raw_data=input('would you like to see raw data?\n').strip().lower()
        start=0
        end=5
        while want_raw_data=='yes':
            print(df.iloc[start:end])
            start+=5
            end+=5
            want_raw_data=input('would you like to see more of raw data?\n').strip().lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n').strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()