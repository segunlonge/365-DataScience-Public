# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 12:35:34 2025

@author: slong
"""

'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

class circle(object):
    '''A class to return the area of a circle. Note that instead of hard
    coding the value of Pi the maths module can be imported to use the default
    Pi value
    
    See course solution for comprehensive answer
    '''
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        area = (self.radius**2)*3.14
        print(f'''Area of circle with radius: {self.radius} is: {area}''')
        
circle_1 = circle(8)
circle_1.calculate_area()
