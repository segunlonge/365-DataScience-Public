# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:03:30 2025

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
        
        Student.total_students +=1 # Increment the total_students count
        
    # Please, modify *only* the text within the curly braces.
    # Any extra spaces or newlines will lead to an *incorrect* answer.
    def get_details(self):
      print(f'''Name: {self.name}
            Age: {self.age}
            Major: {self.major}
            GPA: {self.gpa}
            Year: {self.year}
            
            Total number of students in class: {self.total_students}''')

# Create an instance of the Student class
student1 = Student(
  name="Aisha Khan",
  age=19, 
  major="Biology", 
  gpa=3.9, 
  year=2
  )

# Output the total number of students
student1.get_details()