books = []  # Create an empty list

for i in range(5):
    book = input("Enter your favorite book: ")  # GET the book and store it in 'book'
    books.append(book)  # ADD the 'book' to the list 'books'

print("\nHere are your favorite books:")

for book in books:
    print(f"- {book}")  # Print each book on a new line
