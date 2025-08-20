# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:08:16 2025

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

# step 3: generate a random sample of 100 data points from a normal distribution

#loc = mean; scale = standard deviation and size = number of samples
data = np.random.normal(loc=0, scale=1, size=100)

# step 4: visualizing the data
# alpha parameter controls transparency of plotted elements and takes value between 0 and 1
plt.hist(data, bins=10, alpha=0.7, color='blue')
plt.title('Histogram of Sample Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# step 5: Performing a Hypothesis Test
# hypothesis testing allows you to make inferences about population parameters

# perform one-sample t-test i.e. mean = 0 (null); mean not equal to 0 (alternative)
'''
(the t-test is the same as z-test but used regardless of the population distribution,
 however it does require the sample size to be large because it uses the Central Limit Theorem.
 However when the sample size is not large i.e. n < 25 then the population distribution has to be
 normal
 
 Also, the one-sample t-test refers to the fact that we are considering a single mean and sample as opposed to
a two-sample t-test which is concerned with differences between parameter values on the basis of two independent samples of
data)
'''

t_statistic, p_value = stats.ttest_1samp(data, 0)
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# step 6: Interpreting the results

'''
The p-value is quite large {p>0.1} so there is little or no evidence against
the null hypothesis and so we accept the null hypothesis.

The T-statistic value  indicates how far your sample mean is from the null
hypothesis mean, measured in standard errors. In this example the t-statistic is: 0.96318
''' 

# step 7: Performing Additional Statistical Tests
# -- comparing the means of two independent samples (use independent t-test)

# generate another sample
data2 = np.random.normal(loc=0.5, scale=1, size=100)

# perform independent t-test
t_statistic, p_value=stats.ttest_ind(data, data2)
print("T-statistic (two-sample):", t_statistic)
print("P-value (two-sample):", p_value)


# step 8: Using Confidence Intervals (for the 1 sample)

'''the definition of a 95% confidence interval implies that if
the sampling procedure were repeated a large number of times, then about
5% of the intervals generated in this way would miss the population mean
completely.
'''

confidence_level = 0.95
degrees_freedom = len(data) - 1
sample_mean = np.mean(data)
sample_standard_error = stats.sem(data)

confidence_interval = stats.t.interval(confidence_level, degrees_freedom, loc=sample_mean, scale=sample_standard_error)
print("95% Confidence interval:", confidence_interval, "| With sample mean:", sample_mean )

