# Provided dictionary of students and their grades
grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Fay": 90,
    "Grace": 77,
    "Hank": 95
}

# Step 1: Print Alice's grade
print("Alice's grade is:", grades['Alice'])

# Step 2: Add Eve to the system
grades['Eve'] = ''

# Step 3: Update Bob's grade to 95
grades['Bob'] = '95'

# Step 4: Remove Charlie from the system
del grades['Charlie']

# Step 5: Print all students and their grades by cycling through the key, value pair
for student, grade in grades.items():
    print(f"Student {student} has a grade of {grade}")

# Step 6: Check if David is still in the system
if 'David' in grades:
    print("David is in the system")
else:
    print("David is not in the system.")
