# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 12:40:43 2025

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
import numpy as np
import matplotlib.pyplot as plt

# Project 1: Comparing two sample means

'''
Objective: Perform a t-test to determine if there is a significant difference 
between the means of two independent samples
'''

'''
The z-test can be used for testing hypotheses regarding the population
mean, regardless of the population distribution but it does, however, require
the sample size to be large because it uses the Central Limit Theorem.

when the sample size is not large (which by the rule of thumb means that n < 25) then the
t-test can be used providing the population distribution is normal.

'''

# Step 1: Generate two random samples

# Setting NumPy's random number generator with a starting seed of 0 for reproducability
np.random.seed(0)

# loc is the mean
# scale is the standard deviation
# size is the number of random numbers
sample1=np.random.normal(loc=50, scale=10, size=100)
sample2=np.random.normal(loc=55, scale=10, size=100)


# Step 2: visualise the data by plotting
# alpha parameter controls transparency of plotted elements and takes value between 0 and 1
plt.hist(sample1, alpha=0.5, label='Sample 1', bins=20)
plt.hist(sample2, alpha=0.5, label='Sample 2', bins=20)
plt.legend()
plt.title('Histogram of Two Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Step 3: Perform the t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print(f"T-statistic:{t_stat}, P-value:{p_value}")

'''
The null hypothesis is: mean = 0 and the alternative hypothesis is mean <> 0
As the p value is less than 0.01 there is strong evidence against the null hypothesis
and we can conclude that there is a difference between the mean

Note: The test statistic is examined using the null distribution (i.e. the distribution
of the test statistic under the assumption that the null hypothesis is true)

If the test statistic falls within the critical values (at chosen significant levels then we
reject the nulll hypothesis)
'''

