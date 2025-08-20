'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

input_number = int(input("Please type any number between 1 and 5: "))
if input_number < 1 or input_number > 5:
    print("Input out of range")
elif input_number == 1:
        print("One")
elif input_number == 2:
    print("Two")
elif input_number == 3:
    print("Three")
elif input_number == 4:
    print("Four")
elif input_number == 5:
    print("Five")
#print(input_number)