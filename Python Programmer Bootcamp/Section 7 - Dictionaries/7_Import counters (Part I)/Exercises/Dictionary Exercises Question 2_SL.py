# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 19:46:50 2025

@author: slong
"""

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''

#create an empty dictionary
Fib_seq_12 = {}

'''
Create a list of the first 12 Fibonacci sequence
Code resuse from: "Question 7 For Loops SL.py"
'''

#Initialise the first the numbers of the Fibonacci sequence into a list
Fib_List = [0,1]
#the counter for incrementing the next sequence so the last two numbers are added together
n = 0
#the counter for interating for i sequences 
i = 0

while i < 10:
    #index the last two numbers in the list and add them together
    Next_Num = Fib_List[n] + Fib_List[n+1]
    #print(Next_Num)
    #appended the newly added number as the next sequence 
    Fib_List.append(int(Next_Num))
    n += 1
    i += 1
#print the fib list
print("List of first 12 Fibonacci numbers: ", Fib_List)

'''
Convert the list into a dictionary.
Use the enumerate function on the list of 12 Fib generated numbers to
assign sequenctial keys to each of the Fib numbers from the List
 
'''

#print a new line to separate the two outputs
print("\n")

#use enumerate to assign keys to the values from the list so as to form a dictionary. Start key at 1
Fib_seq_12 = dict(enumerate(Fib_List, start=1))
print("Dictionary of the first 12 Fibonacci numbers: ", Fib_seq_12)





