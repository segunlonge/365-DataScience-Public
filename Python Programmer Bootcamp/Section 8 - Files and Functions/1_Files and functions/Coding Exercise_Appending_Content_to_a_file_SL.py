# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 16:47:16 2025

@author: slong
"""

# Given example.
f = open('poem.txt', 'w')
f.write("The woods are lovely, dark and deep,\n")
f.write("But I have promises to keep,\n")
f.close()

# Step 1: Append a new line to the file 
f = open('poem.txt','a')
f.write('And miles to go before I sleep.\n')
f.write('— Robert Frost\n')
f.close()

# Step 2: Read and print the entire file content
f = open('poem.txt', 'r')
content = f.read()
print(content)
f.close()
