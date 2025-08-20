'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

#initialize the list
input_number_list = []
#initialise the variable
exit_option = "n"

#while the user has chosen n not to exit keep the loop running to ask for more numbers
while exit_option.lower() != "y":
    #ask the user to enter a number
    input_number = input("Please enter a number: ")
    #while the input is not a digit keep asking for a digit until one is enter then 
    #ad it to the list variable
    while not input_number.isdigit():
        input_number = input("Again, please enter a number: ")
    else:
        input_number_list.append(int(input_number))
    #ask the user if they would like to enter more digits
    exit_option = input("Please type y to exit or n to continue entering more digits8: ")
print("The input list of numbers are :" +str(input_number_list), end='\n')

#calculate the avrage from the list
mean_value = sum(input_number_list)/len(input_number_list)
print("The average number is : " +str(mean_value))
