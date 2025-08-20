'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''

users_name = input("Please enter your name: ")

if len(users_name) > 5:
    print("Your name is " + str(len(users_name)) + " Characters long")
else:
    print("Your name is a secret")