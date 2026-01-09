# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:30:12 2025

@author: slong
"""

'''
In this exercise, you will study a Python function that generates all possible permutations of a list of integers. 
Generating all permutations has a time complexity of O(n!) because for a list of n elements, 
there are n! possible unique arrangements.

Investigate the function generate_permutations(numbers) that takes a list of integers numbers as input. 
The function returns a list of lists, where each inner list represents a unique permutation of numbers. 
To keep it simple, we have used Python's built-in itertools.permutations function.

Note: Keep in mind that the number of permutations grows very quickly with the size of n, 
so test with small inputs (like n =< 4) to avoid timeouts.
'''

from itertools import permutations

def generate_permutations(numbers):
    # Generate all permutations using itertools
    return [list(p) for p in permutations(numbers)]

# Test the function with example data
numbers = [1, 2, 3]
print(f"All permutations of {numbers}: {generate_permutations(numbers)}") # Call the function with the list "numbers" passed as an argument