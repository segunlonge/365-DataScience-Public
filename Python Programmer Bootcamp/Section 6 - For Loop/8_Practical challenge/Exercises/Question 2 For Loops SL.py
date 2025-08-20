'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
#input prompt to take value of string
input_string = input("Please type in a string: ")

#convert the input string to a list
input_string_list = list(input_string)
#reverse the order of the list
input_string_list.reverse()

#print each item in the reversed list
#note end='' which allows each item in the list to be printed on the same line
for i in input_string_list:
    print(i, end='')


