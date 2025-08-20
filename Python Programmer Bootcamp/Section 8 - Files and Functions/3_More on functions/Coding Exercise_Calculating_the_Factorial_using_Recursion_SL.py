# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 17:31:08 2025

@author: slong
"""

# Define the recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
        
    else:
        return n * factorial(n - 1)
# Test the function
result = factorial(5)
print("Factorial of 5 is:", result)