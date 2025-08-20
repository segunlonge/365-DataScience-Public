# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 16:48:53 2025

@author: slong
"""

# Step 1: Define the calculate_mean function

def calculate_mean(first, *remainder):
    mean = (first + sum(remainder))/(1 + len(remainder))
    
    if mean == 0:
        print("No values provided")
    else:
        return mean
    

# Step 2: Test the function
print("The mean of 10, 20, 30 is:", calculate_mean(10,20,30))
print("The mean of 5, 15, 25, 35, 45 is:",calculate_mean(5,15,25,35,45))


'''
efficient code
'''

# Step 1: Define the calculate_mean function
def calculate_mean(*args):
    if len(args) == 0:
        return "No values provided"
    mean = sum(args) / len(args)  
    return mean 

# Step 2: Test the function
print("The mean of 10, 20, 30 is:", calculate_mean(10, 20, 30))
print("The mean of 5, 15, 25, 35, 45 is:", calculate_mean(5, 15, 25, 35, 45))
