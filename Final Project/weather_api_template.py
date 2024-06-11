###############################################################################
#                       Final Project 
#                    CSCI 203 Fall 2020
#
# Krystell Ewing
# 11/6/2020
#
# Part 1 Tasks
# 1 - Write methods in CurrentWeather Class
#          __repr__(self)
#          effective_temp(self)
#          __eq__(self, other)
#          __lt__(self, other)
#          __gt__(self, other)
#          copy_city_weather(self)
# 2 - Write methods in Weather Class
#          __repr__(self)
#          add_single_city_weather(self, city_weather)
#          add_weather_from_file(filename)
#          find_coldest_city(self)
#          copy_weather(self)
#          make_warm_temp_list(self, temp_min)
# 3 - Write function print_warm_cities(warm_list, temp_min)
###############################################################################

# Import libraries

import requests
import json
import csv

###############################################################################

#  HELPER FUNCTIONS - ALREADY DONE FOR YOU

###############################################################################

def read_file(filename):
    '''
    DO NOT TOUCH. This is already completed for you.
    
    Reads longitude and latitude data from a csv file
    Stores location (city and state), latitude and longitude in lists
    
    csv file from:
    https://simplemaps.com/data/us-cities
    
    csv file format:
    0(City), 2(State), 6(latitude), 7(longitude)
    
    Parameter 
        filename: a string
    
    Returns: 
        location, a list of strings with city and state
        latitude, a list of strings of the latitude of the locations
        longitude, a list of strings of longitude of the locations
    '''

    # Initialize lists
    location = []
    lat = []
    long = []
    
    # Column locations for city, state, latitude, and longitude data
    CITY = 0
    STATE = 2
    LATITUDE = 6
    LONGITUDE = 7
    
    
    with open(filename, newline='') as csvfile:         # creates a file object
        csvreader = csv.reader(csvfile, delimiter=',')  # set for reading csv file
        
        next(csvreader)                                 # skips header
        
        for row in csvreader:                           # read data
            # Check that all fields are present
            if row[CITY] and row[STATE] and row[LATITUDE] and row[LONGITUDE]:
                # Create a string that includes the city and state
                location.append( row[CITY] + ', ' + row[STATE] )
                # Create lists of strings for latitude and longitude of the location
                lat.append( row[LATITUDE] )
                long.append( row[LONGITUDE] )
                
    return location, lat, long


def print_data(location, lat, long):
    '''
    DO NOT TOUCH. This is already completed for you.
    
    Print the location, latitude, and longitude
    
    Return: None
    '''
    
    # Print header
    print("-" * 40)
    print("{:^20s}{:^10s}{:^10s}".format("Location", "Latitude", "Longitude"))
    print("-" * 40)
    
    # Print values
    for i in range(len(location)):
        print("{:^20s}{:^10s}{:^10s}".format(location[i], lat[i], long[i]))


def get_data(lat, long):
    '''
    DO NOT TOUCH. This is already completed for you.
    
    Returns weather data from api.weather.gov
    
    Parameters:
        lat, a string, the latitude of a location
        long, a string, the longitude of a location
        
    Return values:
        temp, an integer, the current temperature
        temp_unit, a string, the unit for the measured temperature
        wind, an integer, the wind speed in mph
        date_time, a string, in the format of yyyy-mm-dd T hr:min:sec-time zone
        forecast, a string, the current forecast, the short version
    '''
    
    # API URL for week of daily forecasts
    api_url = "https://api.weather.gov/points/" + lat + "," + long + "/forecast/hourly"

    # Insure that keys "properties" and "periods" exist
    while True:
        # data is a dictionary
        data = requests.get(api_url).json()
        # If keys not present, data requested again
        if "properties" in data:
            if "periods" in data["properties"]:
                break
            
    # weather_list contains hourly forecasts for the week
    weather_list = data["properties"]["periods"]
    
    # weather_list[0] is a dictionary of current weather
    current = weather_list[0]

    # Retrieve data from the dictionary current
    temp = current['temperature']
    temp_unit = current['temperatureUnit']
    wind_string = current['windSpeed']
    wind = int(wind_string[:-4])
    date_time = current['startTime']
    forecast = current['shortForecast']

    return temp, temp_unit, wind, date_time, forecast


###############################################################################
#
#     WRITE METHODS FOR THE CurrentWeather class
#
###############################################################################

class CurrentWeather:
    '''    
    Class to hold weather data for an individual city
    '''

    def __init__(self, date_time, location, temperature, temp_unit, wind, forecast):
        '''
        DO NOT TOUCH. This is already completed for you.
        Creates instance of CurrentWeather
        '''
        self.date_time = date_time  # string in form of yyyy-mm-dd hr:min:sec time zone
        self.loc = location         # string with city and state
        self.temp = temperature     # integer, measured temperature
        self.temp_unit = temp_unit  # string, usually F
        self.wind = wind            # int, wind speed in mph
        self.forecast = forecast    # string, short form of the forecast


    def __repr__(self):
        ''' TODO PART 1
        Returns a string representation of an instance of the CurrentWeather class
        '''
        temp_str = str(self.temp)
        wind_str = str(self.wind)
        s =50*"-" + "\n" + self.loc + " Weather \n for " + self.date_time 
        t = "\n Temp F   " + "\t" + temp_str + "\n Wind mph" + "\t" + wind_str + "\n Forecast" + "\t" + self.forecast
        print(40 * "-")
        return s + t
   
        
        

    def effective_temp(self):
        ''' TODO PART 1
        Returns the effective temperature
            calculated from temperature in deg F and wind speed in mph
        Ref: https://www.weather.gov/media/epz/wxcalc/windChill.pdf
        '''
        if self.temp < 50 and self.wind > 3:
            eff_temp = 35.74 + 0.6215 * self.temp - 35.75 * ( self.wind ** 0.16) + 0.4275 * self.temp * ( self.wind ** 0.16)
            return eff_temp
        return self.temp
   
    def __eq__(self, other):
        ''' TODO PART 1
        Overloading of == operator
        
        Parameter: 
            other, another member of the CurrentWeather class
        
        Returns:
            True if the effective temperatures
                of self.temp and other.temp are equal
            Otherwise, returns False
        '''
        if self.effective_temp() == other.effective_temp():
            return True
        return False
    
    
    def __lt__(self, other):
        ''' TODO PART 1
        Overloading of < operator
        
        Parameter:
            other, another member of the CurrentWeather class
        
        Returns: 
            True if the effective temperature of self.temp
                is greater than that of other.temp 
            Otherwise, returns False
        '''
        if self.effective_temp() < other.effective_temp():
            return True
        return False
    
    
    def __gt__(self, other):
        ''' TODO PART 1
        Overloading of > operator
        
        Parameter:
            other, another member of the CurrentWeather class
        
        Returns:
            True if the effective equivalent temperature of self.temp
                is less than that of other.temp 
            Otherwise, returns False
        '''
        
        # Find the effective temperature for self and other        
        if self.effective_temp() >  other.effective_temp():
            return True
        return False

    
    def copy_city_weather(self):
        ''' TODO PART 1
        Returns a deep copy of an instance of the CurrentWeather class
        '''
        new_weather = CurrentWeather(self.date_time, self.loc, self.temp, self.temp_unit, self.wind, self.forecast)
        return new_weather

###############################################################################
#
#     WRITE METHODS FOR THE Weather class
#
###############################################################################

class Weather:
    '''    
    Class to collect instances of the CurrentWeather class in a list
    '''
    
    def __init__(self):
        '''
        DO NOT TOUCH. This is already completed for you
        
        Creates an instance of the Weather class
        '''
        self.all_weather = [] # List to hold instances of CurrentWeather
    

    def __repr__(self):
        ''' TODO PART 1
        Returns a string representation of an instance of the Weather class
        '''
        s = "Weather for All Cities \n"
        for weather in self.all_weather:
            s += weather.__repr__() + '\n'
        print(40 * '*')
        return s
    
    def add_single_city_weather(self, city_weather):
        ''' TODO PART 1
        Method to add a single instance of the 
        CurrentWeather class to the list self.all_weather
        Parameter:
            city_weather, an instance of the CurrentWeather class
        '''
        self.all_weather.append(city_weather)
        
        
    
    def add_weather_from_file(self, filename):
        ''' TODO PART 1
        Method to add instances of the CurrentWeather class
        to the list self.all_weather
        
        Parameter: 
            filename, a string, provides the name of the csv file
                with location, latitude, and longitude data obtained from 
                https://simplemaps.com/data/us-cities
        
        For each location in filename, an instance of the 
        CurrentWeather Class is added to self.all_weather
        '''
        
        # Obtain location( city and state) and latitude and longitude
        location, lat, long = read_file(filename)
        print_data(location, lat, long)
        
        # For each location, add an instance of CurrentWeather to self.all_weather
        
        ##### Help from Help Session #####
        
        for i in range(len(location)):
            temp, temp_unit, wind, date_time, forecast = get_data(lat[i], long[i])
            instance = CurrentWeather(date_time, location[i], temp, temp_unit, wind, forecast)
            self.all_weather.append(instance)
            print("Loaded data from ", location[i])

            
    def find_coldest_city(self):
        ''' TODO PART 1
        Returns the city with the lowest effective temperature
        Return:
            coldest city, an instance of the CurrentWeather class,
                with the lowest temperature of all the instances
                in the list self.all_weather
        '''
        
        ##### Help from Class15 Slides #####
        
        coldest_city = self.all_weather[0]
        for i in self.all_weather:
            if i < coldest_city:
                coldest_city = i 
        return coldest_city
          
               

    
    def copy_weather(self):
        ''' TODO PART 1
        Make a deep copy of an instance of the Weather class
        
        Return:
            other, an instance of the Weather class, a list with
            copies of all of the instances of the CurrentWeather class
            in the list all_weather
        '''
        other = Weather()
        
        other.weather = []
        
        for weather in self.all_weather:
            instance_copy = weather.copy_city_weather()
            other.add_single_city_weather(instance_copy)
        return other
  
    
    def make_warm_temp_list(self, temp_min):
        ''' TODO PART 1
        Recursive function that adds instances of CurrentWeather
        from self.all_weather to a list when the temperature of the 
        CurrentWeather instance is above the temperature temp_min
        
        Parameter:
            temp_min, an integer, a temperature
        
        Return:
            a list of instances of CurrentWeather with
            temperatures above the temperature temp_min
            
        MAKE A COPY OF THE WEATHER CLASS TO USE WITH THIS FUNCTION
        Do NOT use an instance of the Weather class that 
        you need in the future.
        THE FUNCTION ALTERS self.all_weather
        '''
        ##### Help from Prof. Baish email #####
    
        if self.all_weather == [] :
            return []
        else:
            smallest = self.all_weather[0]
            rest = self.all_weather[1: ]
            if temp_min < smallest.temp:
               copy_city_weather = smallest.copy_city_weather()
               self.all_weather = rest
               return [copy_city_weather] + self.make_warm_temp_list(temp_min)
            else:
               self.all_weather = rest
               return self.make_warm_temp_list(temp_min)
            
          
    
    
def print_warm_cities(warm_list, temp_min):
    ''' TODO PART 1
    Print the cities in warm_list with temperatures above temp_min
    
    Parameters
        warm_list, a list of instances of the CurrentWeather class
            with temperatures above temp_min
        temp_min, an integer, a temperature 
        
    Return: None
    '''
    print(50*"-")
    print("Cities with Temperatures over " + str(temp_min) + " deg F")
    print('{:^30s}'.format("City" + "\t" + "Temperature (deg F)"))
    print(50*"-")
    
    
    for cities in warm_list:
        print('{:^30s}{:^30s}'.format(cities.loc , (str(cities.temp))))

def print_coldest_city(coldest_city):
    '''
    Prints results name and temp for the coldest_city
    
    Parameter
        coldest_city, an instance of CurrentWeather
        
    Return: None
    '''
    print(50*'*')
    print('{:^50s}'.format("The coldest city is: " + coldest_city.loc))
    print('{:^50s}'.format("with a temperature of " + str(coldest_city.temp)+ ' deg ' + coldest_city.temp_unit))
    print(50*'*')    
        
###############################################################################
#
#     main function is written for you
#
#     Uncomment print lines when you have other methods/functions written
#    
###############################################################################

def main():
    '''
    Coordinates the functions in Part 1
    
    Prints the results for
        -creating an instance of the Weather class
        -finding the coldest city
        -finding all cities with temperatures above a minimum value
        
    Return: None
    '''
    
    # Weather Class
    # Create an instance of the weather class
    all_cities = Weather()
    # Populate the Weather class with instances of the CurrentWeather class
    filename = 'us_cities_10.csv'
    all_cities.add_weather_from_file(filename)
    # Print the instance of the Weather Class
    # Uncomment following line in when you have the other methods written
    print(all_cities)

    
    # Find the coldest city in the Weather class
    coldest_city = all_cities.find_coldest_city()
    # Print the coldest city in the Weather class
    # Uncomment following line in when you have the other methods written
    print_coldest_city(coldest_city)


    # Make a deep copy of the Weather instance
    copy_cities = all_cities.copy_weather()
    # Set minimum temperature
    temp_min = 70
    # Find the cities with temperature above temp_min
    # Uncomment following line in when you have the other methods written
    warm_list =  copy_cities.make_warm_temp_list(temp_min)
    # Print all cities with current temperature over temp_min
    # Uncomment following line in when you have the other methods written
    print_warm_cities(warm_list, temp_min)


#main()
