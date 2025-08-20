# =============================================================================
# In this exercise, you’ll analyze the character frequency in a provided text using Python's Counter from the collections library, 
# then perform additional transformations to refine the data.
# 1. Use Counter on the lowercase version of the text variable to count each character’s occurrences.
#     - Print the character count
# 2. Convert the result of the Counter operation into a dictionary named new_dict.
# 3. Using a dictionary comprehension, filter new_dict to keep only alphabetic characters.
#     - Print the alphabetic-only count
# =============================================================================

from collections import Counter

# Provided text data
text = """In data science, we often use machine learning models to predict outcomes based on input data.\n
Machine learning can be classified into three main types: supervised, unsupervised, and reinforcement learning.\n
Supervised learning involves training a model on labeled data, where the correct answer is already known.\n
In contrast, unsupervised learning finds patterns or structures within data without any labeled output.\n
Reinforcement learning is based on rewarding a model for making correct decisions and penalizing it for mistakes.\n
By understanding these types, we can choose the right model for our data and improve our predictions."""

# Step 1: Count all characters using Counter on lowercase text
''' 
Using the Counter method is a quicker way to count all the characters in a text as opposed
to using some kind of for loop
'''

print("Character counts:", Counter(text.lower()))

# Step 2: Convert Counter to dictionary
'''
Converts the counter wrapper into a dictionary
'''

new_dict = dict(Counter(text.lower()))

# Step 3: Filter only alphabetic characters

new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}
print("Alphabetic character count:", new_dict)

'''
Illustrates an example of cycling through key value pairs in a dictionary
'''
