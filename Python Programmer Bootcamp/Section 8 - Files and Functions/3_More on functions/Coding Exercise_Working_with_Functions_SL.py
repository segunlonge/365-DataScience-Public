# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 16:28:28 2025

@author: slong
"""

# Step 1: Define a function to display a welcome message

def welcome_message():
    print("Welcome to the Python Programmer Bootcamp!")
    
# Step 2: Define a function to greet with a name, defaulting to "Guest"

def greet(name='Guest'):
    print(f'Hello, {name}! Great to have you here!')

# Step 3: Call the functions
welcome_message()
greet()
greet("Alex")
