'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
#nested for loop count 1 to 12 and within each one count another 1 to 12
for j in range(1,13):
    print(str(j)+ "times table")
    for i in range(1,13):
        Answer = j*i
        #concatenate numbers and string and print each out on a new line
        print(str(j)+ " X " +str(i)+ " = " +str(Answer), end='\n')
    print("")

