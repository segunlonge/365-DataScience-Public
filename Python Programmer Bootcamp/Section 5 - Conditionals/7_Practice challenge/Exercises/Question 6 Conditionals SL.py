'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''

int_1 = input("Please type in your first integer: ")
int_2 = input("Please type in your second integer: ")

if int_1.isdigit() and int_2.isdigit():
    print("Both integers are digits")
    print(int_1,int_2)
    # swap values 
    int_1,int_2 = int_2,int_1
    print(int_1,int_2)
    
    

