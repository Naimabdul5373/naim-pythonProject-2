books = []

for i in range(5):
    book = input("enter your favorite book:")
    books.append(book)
    
    print("\n here is your favorite books:")
    
    for book in books:
        print(f"- {book}")
    