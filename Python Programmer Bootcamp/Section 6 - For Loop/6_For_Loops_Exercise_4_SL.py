# Provided list
my_list = [10, 20, 33, 45, 49, 44, "banana", 51, 66, 78, 99]

# Step 1: Remove the banana
my_list.remove("banana")
print("After removing 'banana':", my_list)

# Step 2: Append 100 to the list
my_list.append(100)
print("After append:", my_list)

# Step 3: Reverse the list
my_list.reverse()
print("After reverse:", my_list)

# Step 4: Extend the list with [2, 1]
my_list.extend([2,1])
print("After extend:", my_list)

# Step 5: Find the index of 66
index_of_66 = my_list.index(66)
print("Index of 66:", index_of_66)
