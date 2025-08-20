# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 18:07:40 2025

@author: slong
"""

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''

import string, random, matplotlib.pyplot as plt

english_alphabet = []
random_numbers = []

# loop through the english alphabet and create a list from a to z
# create a random number between 1 and 25 inclusive for each letter in the english alphabet and assign to a list
for letter in string.ascii_lowercase:
    #print(letter)
    english_alphabet.append(letter)
    # Note: convert integer to string to be abble to use the zip function
    random_numbers.append(str(random.randint(1,25)))
#print(english_alphabet)
#print(random_numbers)

# Example: combining two lists into a key value pair
# =============================================================================
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# 
# combined = dict(zip(keys, values))
# print(combined)
# =============================================================================

# zip the two lists into a key-value pair
english_dictionary = dict(zip(english_alphabet, random_numbers))
print(english_dictionary)

# split the dictionary into two separate tuples
# use zip to combine the first elements of each tuple and assign them to the x and y variable
x,y = zip(*english_dictionary.items())
plt.bar(x,y)


# Draw a bar graph of the english_dictionary dictionary
plt.bar(x,y)
plt.xlabel('english alphabets')
plt.ylabel('random numbers')
plt.title('Bar Graph of alphabet and random numbers')
plt.show()
