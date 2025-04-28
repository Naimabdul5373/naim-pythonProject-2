import matplotlib.pyplot as plt  # type: ignore

# Step 1: Collect books and ratings
books = []
ratings = []

for i in range(10):
    book = input("Enter your favorite book: ")
    rating = int(input(f"On a scale from 1 to 10, how much do you love '{book}'? "))
    
    books.append(book)
    ratings.append(rating)

# Step 2: Show the list
print("\nHere are your favorite books with ratings:")
for book, rating in zip(books, ratings):
    print(f"- {book}: {rating}/10")

# Step 3: Create the Bar Graph with COLORS
colors = ['red','blue','green','yellow','pink','black','purple','white','grey','lavender']

plt.bar(books, ratings, color=colors[:len(books)])  # <<< Add color= here
plt.title("Favorite Books and Their Ratings")
plt.xlabel("Books")
plt.ylabel("Ratings (1-10)")
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.tight_layout()       # Adjust layout
plt.show()               # Show the bar graph

# Step 4: Create the Pie Chart
plt.pie(ratings, labels=books, autopct='%1.1f%%', startangle=140)
plt.title("Favorite Books - Pie Chart")
plt.axis('equal')  # Make it a perfect circle
plt.tight_layout()
plt.show()         # <<< Add this to show pie chart!
Button(Which Window, text = 'Enter The Text').grid(row = Which Row, column = Which Column)