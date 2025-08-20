
'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''

first_integer = input("Please type in your first integer: ")
second_integer = input("Please type in your second integer: ")

#use isdigit to check if input is an integer
if first_integer.isdigit() and second_integer.isdigit():
    print("Both integers are digits")
    first_integer = int(first_integer)
    second_integer = int(second_integer)
    if first_integer > 20 or first_integer < 20 or second_integer > 20 or second_integer < 20:
        print("Input out of range, both digits must be between 1 and 20")
    if first_integer > 15 and second_integer > 15:
        product = first_integer*second_integer
        print(product)
    elif first_integer > 15 or second_integer > 15:
        product = first_integer + second_integer
        print(product)       
    else:
        print("One or more of the digits is less than 15")
        print(0)
else:
    print("One or more of the integers is not a digit")
