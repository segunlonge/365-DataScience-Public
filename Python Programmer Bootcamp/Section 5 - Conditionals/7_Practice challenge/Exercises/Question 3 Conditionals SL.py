'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''

import random

random_number = random.randint(1, 10)
print(random_number)


users_number = input("Guess a number between 1 and 10: ")

# Check if the input is a digit
if users_number.isdigit():
    users_number = int(users_number)
    if users_number == random_number:
        print("You guessed the correct number as " +str(users_number))
    elif users_number != random_number:
        print("You did not guess the correct number")
else:
    print("Please ensure you input a digit")
