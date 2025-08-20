'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
#create the blue-print for printing the pattern
Pattern_List = [5,1,4,1,1,1]

#loop through the blue-print getting the index of each code used to print the pattern
for i in range(len(Pattern_List)):
    print("*"*Pattern_List[i])
    
