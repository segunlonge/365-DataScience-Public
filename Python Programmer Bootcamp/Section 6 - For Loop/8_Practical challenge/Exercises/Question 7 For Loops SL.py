'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

#tnitialise the first the numbers of the Fibonacci sequence into a list
Fib_List = [0,1]
#the counter for incrementing the next sequence so the last two numbers are added together
n = 0
#the counter for interating for 18 sequences 
i = 0

while i < 18:
    #index the last two numbers in the list and add them together
    Next_Num = Fib_List[n] + Fib_List[n+1]
    #print(Next_Num)
    #appended the newly added number as the next sequence 
    Fib_List.append(int(Next_Num))
    n += 1
    i += 1
#print the fib list
print("List of first 20 Fibonacci numbers: ", Fib_List)
    
    
