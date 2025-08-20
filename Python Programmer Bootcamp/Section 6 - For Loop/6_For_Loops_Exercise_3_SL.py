# Step 1: Create the data list
Data = [45, 12, 78, 34, 89, 23, 44, 50, 66, 4]

# Step 2: Create a copy of the data to keep the original list intact
Data_Copy = Data[:]

# Step 3: Implement bubble sort

# for each number i in the list perform the nested tasks below
for i in range(len(Data_Copy)):
    # for each number j (for each i) in the list (reduce range by i on each loop)
    for j in range(0,len(Data_Copy)-i-1):
        # check if the number j is greater than the number next to it
        if Data_Copy[j] > Data_Copy[j+1]:
            # if that number is greater then the number next to it swap it
            Data_Copy[j], Data_Copy[j+1] = Data_Copy[j+1], Data_Copy[j]
            
# sorted data
print("Manual bubble sort: ",Data_Copy)
# original data
print("Original data: ",Data)

# python's own bubble sort function
print("Python's bubble sort function: ", sorted(Data))


