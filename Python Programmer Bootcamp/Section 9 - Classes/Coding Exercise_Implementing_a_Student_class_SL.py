# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 12:44:11 2025

@author: slong
"""

# Create a Student class with the listed attributes
class Student(object):
    '''A student class and object creator'''
    
    # Class variable; applies to all instances of the student class object
    status = 'student'

    '''The __init__ function (called a constructor)
    creates variables for each instance (from the arguments
    in the brackets) of the class object so that each instance 
    of the object can have it's own variables
     '''
    def __init__(self,name,age,major,gpa,year): # instance variables
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.year = year
        
# Create two instances of the Student class
student1 = Student(
  name="Aisha Khan", 
  age=19, 
  major="Biology", 
  gpa=3.9, 
  year=2
  )

# Create the second instance corresponding to the student Carlos Alvarez
student2 = Student(
    name="Carlos Alvarez",
    age=21,
    major="Mechanical Engineering",
    gpa=3.5,
    year=3)

# Output the details of both students. 
# Please, do not modify the print-functions.
print(f'''Student 1:
Name: {student1.name}
Age: {student1.age}
Major: {student1.major}
GPA: {student1.gpa}
Year: {student1.year}''')

print("")

print(f'''Student 2:
Name: {student2.name}
Age: {student2.age}
Major: {student2.major}
GPA: {student2.gpa}
Year: {student2.year}''')