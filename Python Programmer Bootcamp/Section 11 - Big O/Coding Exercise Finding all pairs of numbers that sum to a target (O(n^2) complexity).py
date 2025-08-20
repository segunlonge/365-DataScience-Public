# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:47:08 2025

@author: slong
"""

'''
When analyzing algorithms with O(n^2), or "quadratic time complexity," we see that the number of operations grows 
proportionally to the square of the input size. This means that if the input size doubles, the time taken by the 
algorithm roughly quadruples; if the input size triples, the time increases by a factor of nine. Quadratic-time 
algorithms can handle small inputs efficiently, but as the input size grows, the number of operations increases 
significantly, making them less practical for large datasets. This rapid growth is a key characteristic of 
O(n^2) complexity.
 
Let's consider a simple example: finding all pairs of numbers in a list that add up to a target sum. To accomplish this, 
we can use a nested loop—one loop to pick the first number and another to check every other number in the list as a potential 
pair. For each element in the list (n elements total), we perform another operations to compare it with every other element. 
This results in approximately n*n comparisons, or n^2 operations in total.
'''

def find_pairs(numbers, target):
  # Initialize a list to store pairs
  pairs = []
  # Outer loop to select the first number
  for i in range(len(numbers)):
      # Inner loop to select the second number
      for j in range(i + 1, len(numbers)):
          # Check if the two numbers add up to the target
          if numbers[i] + numbers[j] == target:
              pairs.append((numbers[i], numbers[j]))
  return pairs

# Test the function with example data
numbers = [2, 4, 3, 5, 7]
target = 9
print(f"Pairs that sum to {target}: {find_pairs(numbers, target)}")