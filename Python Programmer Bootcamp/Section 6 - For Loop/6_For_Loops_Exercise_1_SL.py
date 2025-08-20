# -*- coding: utf-8 -*-
"""
1. Use a for loop to print all even numbers between 1 and 20 (inclusive).
    - Use the range() function with appropriate start, stop, and step values
    
2. Create a variable word and assign it the value "looping"
    - Use a for loop to iterate over the characters in word and point each character on a new line.
"""

for i in range(2,21,2):
    #print each i variable on a new line
    print(i, end='\n')

#print("\n")
    
word = "looping"
for char in word:
    #print each char variable on a new line
    print(char, end='\n')

