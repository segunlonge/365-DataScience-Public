# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:51:28 2025

@author: slong
"""

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''

'''
Statistical Analysis using SciPy
https://medium.com/tomtalkspython/statistical-analysis-using-scipy-6db9fa891903
'''

# import required modules
import scipy.stats as stats
import pandas as pd

# Project 2: Chi-Squared Test for Independence

'''
Objective: Perform a chi-squared test to assess whether two categorical variables are
independent
'''

'''
A Chi-Squared test is typically used to measure how a model compares to the actual
observed data by comparing observed vs expected in a statistical test
'''

# Step 1: Create a contigency table

# A dictionary with two keys (Gender: with a list of gender labels) and (Preference:
# with a list of preferences) 
data = {'Gender': ['Male','Male','Female','Female','Male','Female','Male','Female'],
        'Preference':['Sports','Music','Sports','Music','Music','Sports','Sports','Music']}

df = pd.DataFrame(data)

# The crosstab method produces a table counting how many times each combination of Gender
# and Peference occurs

'''
The cross tab table is often used for:
    1. Descriptive statistics
    2. Chi-squared tests of independence
    3. Analyzing relationships between two categorical variables
'''

contingency_table = pd.crosstab(df['Gender'], df['Preference'])
print(contingency_table, "\n")

# Step 2: Perform the chi-squared test

'''
Assign the outputs of each returned value:
    1. chi2_stat: Test statistic of difference between observed and expected values
    2. P-value: Gives the probability of observing the test statistic within the assumption of the null distribution.
        Often used to reject or accept the null hypothesis. The null distribution is based on the assumption that the null
        hypothesis is true.
    3. DoF: Degrees of Freedom is "how many independent pieces of information go into estimating a parameter"
    4. Expected: The expected values as opposed to the observed values
        
'''
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
print(f"Chi-squared Statistic: {chi2_stat}, P-value:{p_value}")

# Step 3: Interpret the results

'''
Given that the P-value is greater than 0.1 suggests that there is little or no evidence against the null hypothesis
i.e. no difference in between gender preference for sports and music
'''





