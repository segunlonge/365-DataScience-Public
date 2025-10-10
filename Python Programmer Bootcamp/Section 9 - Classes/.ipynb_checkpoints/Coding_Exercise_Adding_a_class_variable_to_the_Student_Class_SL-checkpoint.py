# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 19:05:22 2025

@author: slong
"""

# Create a Student class with the listed attributes
class Student(object):
    # Create a class variable called total_students to keep track of the total number of students. Assign it a value of 0.
    total_students = 0
    
    def __init__(self, name, age, major, gpa, year):
        # Define instance attributes here
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.year = year
        
        Student.total_students += 1 # Increment the total_students count
        
# Create three instances of the Student class
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

# Create the third instance corresponding to the student Maya Patel
student3 = Student(
    name="Maya Patel",
    age=18,
    major="Physics",
    gpa=3.7,
    year=1)
# Output the total number of students
print(f"Total number of students: {Student.total_students}")