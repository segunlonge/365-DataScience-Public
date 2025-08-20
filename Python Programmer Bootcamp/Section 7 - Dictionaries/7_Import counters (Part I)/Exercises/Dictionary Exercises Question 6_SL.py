# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 11:43:32 2025

@author: slong
"""

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

suits_keys = ['Clubs','Diamonds','Hearts','Spades']
cards_list = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

# Example adding a new key with a list as its value
# =============================================================================
# my_dict = {}
# my_list = [1, 2, 3]
# 
# my_dict['numbers'] = my_list
# print(my_dict)
# =============================================================================
# Output: {'numbers': [1, 2, 3]}

# empty dictionary
suits_dictionary = {} 

# for each item in the suits_keys list make a key-value pair with the cards list
for item in suits_keys:
    suits_dictionary[item] = cards_list

# print the required dictionary containing 4 suits of 13 cards    
print(suits_dictionary)
    