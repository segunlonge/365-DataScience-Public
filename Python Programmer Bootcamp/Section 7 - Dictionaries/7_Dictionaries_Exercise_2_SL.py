# Provided lists of numbers and letters
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

# Step 1: Combine numbers and letters lists
combined_alpnum = list(zip(numbers,letters))
print("Combined list of numbers and letters:", combined_alpnum)

# Step 2: Unpack combined_list into two separate lists
x,y = zip(*combined_alpnum)

print("Unpacked list of numbers:", x)
print("Unpacked list of letters:", y)