# =============================================================================
# Imagine you’re working with a digital library system that stores information about books in various categories. 
# Each category contains a list of books, where each book has attributes like title and author. 
# Your task is to access and print specific information from this library system.
#
# 1. Access and print the first fiction book's title
#     - Extract the title of the first book in the fiction category. 
#     - Print it in the format: "First Fiction book title: <title>"
#
# 2. Access and print the author of the second science book.
#     - Extract the author of the second book in the Science category.
#     - Print it in the format: "Second Science book author: <author>"
#
# 3. Display each book in the history category
#     - Loop over each book in the History category.
#     - For each book, print a sentence describing it, 
#     in the format: "In the History category, we have <title> by <author>"
# =============================================================================


#  The provided data
library = {
    "Fiction": [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"}
    ],
    "Science": [
        {"title": "A Brief History of Time", "author": "Stephen Hawking"},
        {"title": "The Selfish Gene", "author": "Richard Dawkins"}
    ],
    "History": [
        {"title": "Sapiens", "author": "Yuval Noah Harari"},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond"}
    ]
}

# Access and print the title of the first Fiction book
print("First Fiction book title:", library['Fiction'][0]['title'])

# Access and print the author of the second Science book
print("Second Science book author:", library['Science'][1]['author'])

# Print each History book's title and author in a formatted sentence
for book in library["History"]:
    print(f"In the History category, we have {book['title']} by {book['author']}")