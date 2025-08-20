# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 20:14:01 2025

@author: slong
"""

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

#create an empty dictionary
share_price = {}

#list of share prices for each company
Python_DS = [12.87, 13.23, 11.42, 13.10]
PythonSoft = [23.54,25.76,21.87,22.33]
Pythazon = [98.99,102.34,97.21,100.065]
Pybook = [203.63,207.54,202.43,205.24]

#sort each of the list (prices) above from highest to lowest
Python_DS = sorted(Python_DS, reverse = True )
PythonSoft = sorted(PythonSoft, reverse = True )
Pythazon = sorted(Pythazon, reverse = True )
Pybook = sorted(Pybook, reverse = True )

# create a list of list of sorted lists from above
super_list = [Python_DS, PythonSoft, Pythazon, Pybook]
#print(super_list)

# create a list of keys to be used for the share price 
pricekeys = ['High', 'Close', 'Open', 'Low']

# create an empty list to store the zip of price keys to prices 
super_list_2 =[]

# for each sub list in the super list zip the pricekeys as keys to the prices (values) into a list called super_list_2
for item in super_list:
    #print(item)
    values = [item]
    # create key value pairs for each price in each sub list from the pricekeys keys
    item = [dict(zip(pricekeys, row)) for row in values]
    #print(item)
    # append each dictionary into a super list
    super_list_2.append(item)
    # Note: super_list_2 contains lists of dictionaries 
    
    
# Example use of dict zip to combine key-value pairs from lists into a dictionary
# =============================================================================
# keys = ['name', 'age', 'city']
# values = ['Alice', 30, 'London']
# 
# result = dict(zip(keys, values))
# print(result)
# =============================================================================
    
#print(super_list_2)
#print(type(super_list_2))

# turns a list into a dictionary with key value pays numbered from 0 sequentially
share_price = dict(enumerate(super_list_2))
#print(share_price)

#create a dictionary with keys and lists of list from the superlist
keys = ['Python_DS', 'PythonSoft', 'Pythazon', 'Pybook']
values = [super_list_2]
my_dict = [dict(zip(keys, row)) for row in values]
print(my_dict)

