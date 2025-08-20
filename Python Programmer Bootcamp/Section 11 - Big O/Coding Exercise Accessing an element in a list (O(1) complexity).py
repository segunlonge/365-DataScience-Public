# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 13:20:38 2025

@author: slong
"""

'''
Although the time complexity of algorithms is typically proven through theoretical analysis, 
we can explore it intuitively with examples to develop an understanding.
 
To begin with, an algorithm with O(1), or "constant time complexity," performs its operation in the same amount of time regardless of the size of the input. 
This means that the number of operations does not increase as the input grows. Constant-time operations are the most efficient in terms of time complexity, 
as their performance remains stable no matter how large the input becomes.
 
A simple example of an O(1) operation is accessing an element in a list by its index. Whether the list has 10 elements or 10 million, 
retrieving the element at a specific index takes the same, fixed amount of time. 
This is because Python’s list structure is implemented in a way that allows direct access to any index without looping through the list.
'''

def get_element_at_index(numbers, index):
  # Check if the index is out of range
  if index < 0 or index > len(numbers):
      return "Index out of range"
  # Access the element at the given index
  return numbers[index]

# Test the function with example data
numbers = [10, 20, 30, 40, 50]
index = 2
print(f"Element at index {index}: {get_element_at_index(numbers, index)}")