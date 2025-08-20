# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:34:00 2025

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
      
    def update_age(self):
      # Implement the update_age() method
      self.age +=1
      
    def update_major(self, new_major):
      # Implement the update_major() method
      self.major = new_major


# Define the HonorsStudent class, inheriting from Student
class HonorsStudent(Student):
    # Define the __init__ method and the instance attributes here
        
    def __init__(self, name, age, major, gpa, year, honors_program):
        super().__init__(name, age, major, gpa, year)
        self.honors_program = honors_program

    # Please, modify *only* the text within the curly braces.
    # Any extra spaces or newlines will lead to an *incorrect* answer.     
    def get_details(self):
      print(f'''Name: {self.name}
Age: {self.age}
Major: {self.major}
GPA: {self.gpa}
Year: {self.year}
Honors Program: {self.honors_program}

Total number of students in class: {self.total_students}''')
      
# Create an instance of the HonorsStudent class
honor_student = HonorsStudent(
  name="David Kim", 
  age=20, 
  major="Computer Science", 
  gpa=3.9, 
  year="Junior", 
  honors_program="STEM Honors"
)

# Output the total number of students
honor_student.update_age()
honor_student.get_details()