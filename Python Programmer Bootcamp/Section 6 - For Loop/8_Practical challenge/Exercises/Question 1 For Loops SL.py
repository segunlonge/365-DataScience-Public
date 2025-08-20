'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
#initiate variable to store count of number
import sys
count_of_number = 0

while True:
    #check to see if input for first_number is a digit and loop until it is a digit
    first_number = input("Please type the first number between 1 and 100: ")
    if not first_number.isdigit():
        print("This is not a digit")
    else:        
        while True:
            #check to see if input for second_number is a digit and loop until it is a digit
            second_number = input("Please type the second number between 1 and 100: ")
            if not second_number.isdigit():
                print("This is not a digit")
            else:
                #convert both inputs to integer
                first_number = int(first_number)
                second_number = int(second_number)
                #test for the validity of numbers entered in prompt are within the range 1 to 100
                #note the "\" character for line continuation
                while first_number < 0 or second_number < 0 or first_number > 100 or second_number > 100 or \
                    first_number == second_number:
                    print("Invalid input, numbers must be between 1 and 100")
                    first_number = input("Please type a number between 1 and 100: ")
                    second_number = input("Please type another number between 1 and 100: ")
                
                #loop between the range of the first and last number counting the gap between and storing it in a variable
                #also, be able to count the gap whether the first number is greater than the second and vice versa
                for i in range(first_number, second_number):
                    if first_number < second_number:
                        count_of_number = count_of_number + 1
                else:
                    if first_number > second_number:
                        for i in range(second_number, first_number):
                            count_of_number = count_of_number + 1
                
                #print the gap/count between the first number and the second number    
                print("Total count from " +str(first_number)+ " to " +str(second_number)+ " is: " +str(count_of_number))
                #necessary to stop the loop of adding previous counts to current count
                sys.exit()