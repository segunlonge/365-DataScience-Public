# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 16:05:20 2025

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

# Project 3: Linear Regression Analysis

'''
You will analyze the relationship between two categorical variables and determine if they are independent.

Linear Regression (a special case of the general regression model) uses the method of least squared i.e.
if a line of the form y = a+bx is to be fitted to data points (xi,yi), then the residual wi for the point
(xi,yi) is the difference between the observed value yi and the value of a+bxi i.e. wi = yi-(a+bxi)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Generate synthetic data

# Using the same seed number on the random number generator ensures the same random sequence
np.random.seed(1)
#print(np.random.rand(100))
x = np.random.rand(100)*10
y = 2.5*x + np.random.randn(100)

# Step 2: Perform linear regression

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(f"Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}")

# Step 3: Visualiz the regression line

plt.scatter(x,y,label='Data points')
plt.plot(x,slope*x+intercept,color='red',label='Regression line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression Analysis')
plt.legend()
plt.show()

# Step 3: Interpret the results
'''
The R-squared value indicates the degree of correlation between the x and y variable; in 
this case the x and y variables are highly correlated given the R-squared value: 0.985.
'''

