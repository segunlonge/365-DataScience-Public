'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''

number_string_list = ['one','two','three','four','five' ]
input_number_string = input("Please type any number in string between one and five: ")

if input_number_string.lower() not in number_string_list:
    print("Number out of range")
elif input_number_string.lower() == 'one':
    print("1")
elif input_number_string.lower() == 'two':
    print("2")
elif input_number_string.lower() == 'three':
    print("3")
elif input_number_string.lower() == 'four':
    print("4")
elif input_number_string.lower() == 'five':
    print("5")
