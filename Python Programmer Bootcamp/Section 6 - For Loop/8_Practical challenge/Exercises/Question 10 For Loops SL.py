'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
#list place holders to store odd and even numbers
odd_numbers = []
even_numbers = []

#loop between 1 and 100 numbers and determine if odd or even and assign to respective list
for i in range(1,101):
    if i%2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Odd numbers between 1 to 100: ", odd_numbers)
print()
print("Even numbers between 1 to 100: ", even_numbers)