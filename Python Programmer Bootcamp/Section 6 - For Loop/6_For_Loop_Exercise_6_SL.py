# Step 1: Initialize variables

n = 1
odd_sum = 0

# Step 2: Use a while loop to sum all odd numbers between 1 and 20

while n < 21:
    if n % 2 != 0:
        odd_sum += n
    #print(n)
    n += 1
        
# Step 3: Print the total sum of odd numbers
print("The sum of odd numbers from 1 to 20 is:", odd_sum)
