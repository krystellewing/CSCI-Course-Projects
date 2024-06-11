# -*- coding: utf-8 -*-
"""
Tests for the Final Project Part 1
Created on Mon Nov  9 02:10:16 2020

@author: smithbsh
"""
from weather_api_template import *


#####################################################################
#
# TESTS FOR effective.temp
#
#####################################################################

def test_eff_temp1():
    """
    Tests when temperature of 80 deg F and wind of 1 mph
    """
    
    # Create an instance of the CurrentWeather class
    ex1 = CurrentWeather("2020-10-30T14:00:00-07:00", "Los Angeles, CA", 80, 'F', 1,'Sunny')
    
    # Determine effective temperature
    test_temp =  ex1.effective_temp()
    
    # Check if test_temp correct
    if (test_temp == 80):
        print("Passed effective temperature test 1")
    else:
        print("Failed effective temperature test 1")

  
def test_eff_temp2():
    """
    Tests when temperature of 80 deg F and wind of 20 mph
    """
    
    # Create an instance of the CurrentWeather class
    ex2 = CurrentWeather("2020-10-30T14:00:00-07:00", "Los Angeles, CA", 80, 'F', 20,'Sunny')
    
    # Determine effective temperature
    test_temp =  ex2.effective_temp()
    
    # Check if test_temp correct
    if (test_temp == 80):
        print("Passed effective temperature test 2")
    else:
        print("Failed effective temperature test 2")

 
def test_eff_temp3():
    """
    Tests when temperature of 40 deg F and wind of 1 mph
    """
    
    # Create an instance of the CurrentWeather class
    ex3 = CurrentWeather("2020-10-30T22:00:00-04:00", "Boston, MA", 40, 'F', 1,'clear')
    
    # Determine effective temperature
    test_temp =  ex3.effective_temp()
    
    # Check if test_temp correct
    if (test_temp == 40):
        print("Passed effective temperature test 3")
    else:
        print("Failed effective temperature test 3")

   
def test_eff_temp4():
    """
    Tests when temperature of 40 deg F and wind of 1 mph
    """   
    
    # Create an instance of the CurrentWeather class
    ex4 = CurrentWeather("2020-10-30T22:00:00-04:00", "Boston, MA", 40, 'F', 20,'clear')
    
    # Determine effective temperature
    test_temp =  ex4.effective_temp()
    
    # Check if test_temp correct
    if (test_temp == 30.4807859131122):
        print("Passed effective temperature test 4")
    else:
        print("Failed effective temperature test 4")
    
#####################################################################
#
# TESTS FOR __eq__
#
#####################################################################
 
def test_eq_1():   
    """
    Tests __eq__ with two instances of CurrentWeather
    that differ only in wind speed
    """
    
    # Create instances of the CurrentWeather class
    ex1 = CurrentWeather("2020-10-30T22:00:00-04:00", "Boston, MA", 30, 'F', 1,'clear')
    ex2 = CurrentWeather("2020-10-30T22:00:00-04:00", "Boston, MA", 30, 'F', 10,'clear')
    
    # Determine if the two instances are equal
    ans = not(ex1 == ex2)
    if (ans):
        print("Passed __eq__ test 1")
    else:
        print("Failed __eq__ test 1")

def test_eq_2():   
    """
    Tests __eq__ with two instances of CurrentWeather
    that differ in location and forecast but have
    the same temperature and wind speed
    """
    
    # Create instances of the CurrentWeather class
    ex3 = CurrentWeather("2020-10-30T22:00:00-04:00", "Chicago, IL", 30, 'F', 10,'sunny')
    ex4 = CurrentWeather("2020-10-30T22:00:00-04:00", "Boston, MA", 30, 'F', 10,'clear')
    
    # Determine if the two instances are equal
    if (ex3 == ex4):
        print("Passed __eq__ test 2")
    else:
        print("Failed __eq__ test 2")


#####################################################################
#
# TEST FOR find_coldest_city
#
#####################################################################


def test_find_coldest_city():
    """
    Tests function find_coldest_city
    Checks for location of coldest city in an instance of the Weather class
    with 5 cities
    """
    
    # Make an instance of the weather class
    weather_1 = Weather()
    
    # Make instances of the CurrentWeather class
    nyc = CurrentWeather("2020-11-08T22:00:00-06:00", "New York, NY", 54, 'F', 1,'Clear')
    la = CurrentWeather("2020-11-08T22:00:00-06:00", "Los Angeles, CA", 51, 'F', 15,'Mostly Clear')
    chicago = CurrentWeather("2020-11-08T22:00:00-06:00", "Chicago, IL", 68, 'F', 10,'Mostly Cloudy')
    philly =  CurrentWeather("2020-11-08T22:00:00-06:00", "Philadelphia, PA", 52, 'F', 0,'Mostly Clear')
    houston = CurrentWeather("2020-11-08T22:00:00-06:00", "Houston, TX", 70, 'F', 5,'Mostly Cloudy')
    
    # Populate the list all_weather with the CurrentWeather instances
    weather_1.all_weather = [nyc, la, chicago, philly, houston]
  
    # Find the coldest city
    coldest_city = weather_1.find_coldest_city()
    
    # Check if correct city found
    if coldest_city.loc == 'Los Angeles, CA':
        print("Passed find_coldest_city test")
    else:
        print("Failed find_coldest_city test")


    
def main():
    """
    Tests of methods from weather_api_template.py
    """
    test_eff_temp1()
    test_eff_temp2()
    test_eff_temp3()
    test_eff_temp4()
    test_eq_1()
    test_eq_2()
    test_find_coldest_city()
    
    
    
main()