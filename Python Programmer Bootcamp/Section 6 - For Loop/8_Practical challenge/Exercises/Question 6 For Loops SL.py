'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

#variable the first number in a factorial that will increment to 15
n = 1
#the first multiple of the factorial that grows by current multiple * n
factorial_15 = 1

#the loop that multiplies ((1xn)xn)....15
while n < 15:
    factorial_15 = factorial_15*(n+1)
    n = n+1

print("15 factorial is: " + str(factorial_15))