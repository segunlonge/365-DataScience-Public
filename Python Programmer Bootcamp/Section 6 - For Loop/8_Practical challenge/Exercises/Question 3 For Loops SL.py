'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

#input function asking for user entry
input_number = input("Please enter a number between 1 and 12: ")

#while loop to check if number is not a digit or not between 1 and 12 _
#loop until correct entry is made
while (not input_number.isdigit()) or  int(input_number) < 1 or int(input_number) > 12 :
    print("Entry is not valid")
    input_number = input("Please enter a number between 1 and 12: ")

#for loop from 1 to 12 multiplying input number for each digit: 1 to 12  
for i in range(1,13):
    Answer = int(input_number)*i
    #concatenate numbers and string and print each out on a new line
    print(str(input_number)+ " X " +str(i)+ " = " +str(Answer), end='\n')
    

