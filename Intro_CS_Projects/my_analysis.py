# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 07:05:41 2020

FINAL PROJECT PART 2 ANALYSIS- DROUGHTS

@author: Krystell Ewing
"""

##### Krystell Ewing, Professor Baish, CSCI 203 #####

import csv
import matplotlib.pyplot as plt


##### Tweaked Read in From Class 34 Example ####

def readDataFile(filename):
    '''
    This function returns lists formed from multiple csv files that contain
        data on certain states dryness and droughts from 2010 to now.
    
    Parameter
        filename: csv files as strings
    
    Returns
        state_list, [ab_dry_list, mod_list, sev_list, ext_list, excep_list]:
            list of lists of strings for states and lists of floats of types 
            of droughts; abnormally dry, moderate, severe, extreme, and 
            exceptional drought
    '''
    STATE = 1  # defining columns to read
    ABNORMALLY_DRY = 3
    MODERATE = 4
    SEVERE = 5
    EXTREME = 6
    EXCEPTIONAL = 7
    state_list = []     # initializing lists for columns
    ab_dry_list = []                            
    mod_list = []   
    sev_list = []
    ext_list = []
    excep_list = []
    
    
                           
    
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',') # splits rows at commas
        next(csvreader)                       # skip header
        for row in csvreader: 
            
            if row[1] and row[3] and row[4] and row[5] and row[6] and row[7]:
                state_list += [row[1]]
                ab_dry_list += [float(row[3])]
                mod_list += [float(row[4])]     # adds data into empty
                sev_list += [float(row[5])]     #  initialized lists
                ext_list += [float(row[6])]
                excep_list += [float(row[7])]
                
                
                
    return state_list, [ab_dry_list, mod_list, sev_list, ext_list, excep_list]

def create_averages(category_list):
    '''
    This function creates averages of the percent areas of each drought 
        category in each list.
    
    Parameters: category_list 
        list of each drought category list per state; 
        5 categories per state, 6 states, so 30 lists
            
    Returns: drought_avg
        the calculated averages of each drought category
    '''
    # Creates the averages, rounds them to two decimal places
    drought_avg = sum(category_list) / len(category_list)
    return round(drought_avg, 2)


def visualize_averages(state_list, d):
    '''
    Visualizes bar graphs per each states drought averages per category

    parameters:
    - state_list: a list of the states as strings
    - d: the dictionaries that contain the state as a key and list of 
        averages by category as values
    '''
   ##### Resource Used: Midterm Project income_template.py ##### 
    
    drought_categories = ['D0', 'D1', 'D2', 'D3', 'D4']
    x = range(len(d[state_list[0]])) # goes through the values in d
    tickLabels = drought_categories
    plt.xticks(x, tickLabels, rotation = 0)
    plt.xlabel('Drought Categories')
    plt.ylabel('Percent Area Averages per Drought Category')
    plt.title(state_list[0] + ' Drought Averages per Category')
    plt.bar(x, d[state_list[0]]) # values of d as x; key of d as y
    plt.show()
    

    

    
        
def main():
    ''' 
    Function call to read in the csv files of the drought percent areas per
        category per state
    
    Creates averages of the drought percent areas per each state and puts 
        them into lists
    '''
    # Goes through each file and reads it into the data read function 
    for filename in ['az.csv','ca.csv','or.csv','tx.csv','pa.csv','me.csv']:
        state_list, category_list = readDataFile(filename)
        
    # Adds the averages into a comma separated list
    # Adds list as a value into an empty dictionary and state string as a key
        new_list = []
        d = {}
        for categories in category_list:
            average = create_averages(categories)
            new_list += [average]
            d[state_list[0]] = new_list
        print(d)
    
        
        visualize_averages(state_list, d)  # Call to visualize_averages
      
main()