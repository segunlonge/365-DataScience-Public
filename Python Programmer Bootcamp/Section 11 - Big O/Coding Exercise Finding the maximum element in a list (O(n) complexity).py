# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 15:23:31 2025

@author: slong
"""

'''
An algorithm with O(n) "linear time complexity," means that the number of operations required grows proportionally with the size of 
the input. In other words, as the input size doubles, the time taken by the algorithm also roughly doubles. 
If the input size triples, the time triples, and so on, maintaining a direct, linear relationship. 
Linear-time algorithms are efficient for moderate-sized inputs, as they scale directly with the size of the data.
 
Let's consider a simple example: imagine a function that takes a list of numbers and finds the maximum value. 
To find the largest number, the function has to examine each element in the list exactly once, making a single pass from start to end. 
As the size of the list grows, the time taken by the algorithm increases proportionally. 
This one-to-one relationship between the size of the input O(n) and the number of operations required (n checks) is what characterizes an 
 time complexity.
'''

def find_max(numbers):
    # Initialize a variable to store the maximum value, start with the first element
    max_value = numbers[0]
    
    # Iterate through the list, comparing each number
    for num in numbers:
        if num > max_value:
            max_value = num            
            
    # Return the largest number found
    return max_value

# Test the function with example data
numbers = [3, 1, 7, 0, 4, 9, 2]
print(f"The maximum value in the list is: {find_max(numbers)}")