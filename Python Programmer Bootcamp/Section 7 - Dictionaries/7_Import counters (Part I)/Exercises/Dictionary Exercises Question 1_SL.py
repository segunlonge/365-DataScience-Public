# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 22:48:26 2025

@author: slong
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

'''
dictionary key/value pairs for countries (key) and their capitals (value)
'''
capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
           'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
           'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
           'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
           }

#user input to get capital city
country = input("Please enter a captial city: ")
#capitalise the user input
country = country.capitalize()


# =============================================================================
# The code snippet {v:k for k, v in myArray.items()} is a dictionary comprehension 
# in Python.
# =============================================================================

    
# Filter the dictionary to only include countries in the `country` list
capitals = {k: v for k, v in capitals.items() if k in country}

#print(capitals)

# If the filtered capitals dictionary is empty state that there are no matching countries found
# else if the capitals dictionary is not empty print its key value pair
if not capitals:
    print("No matching countries found.")
else:
    for country, value in capitals.items():  
        print(f"Country: {country}, Capital: {value}")





