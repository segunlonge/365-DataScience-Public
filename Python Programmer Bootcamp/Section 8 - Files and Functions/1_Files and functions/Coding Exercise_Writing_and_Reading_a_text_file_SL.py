# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:47:16 2025

@author: slong
"""

# Step 1: Open the file in write mode
f = open('story.txt', 'w')

# Step 2: Write content onto the file
f.write('Once upon a time, in a land far, far away,\n')
f.write('there lived a brave young coder.\n')
f.write('This coder loved to solve problems and learn new skills.\n')

# Step 3: Read and display the file content
# Open the file in read mode
f = open('story.txt', 'r')
 
# Read and print the content of the file
print(f.read())
f.close()