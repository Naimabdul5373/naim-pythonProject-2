from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np  # type: ignore

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

plt.bar(books, ratings, color=colors[:len(books)])  
plt.title("Favorite Books and Their Ratings")
plt.xlabel("Books")
plt.ylabel("Ratings (1-10)")
plt.xticks(rotation=45)  
plt.tight_layout()       
plt.show()               

# Step 4: Create the Pie Chart
plt.pie(ratings, labels=books, autopct='%1.1f%%', startangle=140)
plt.title("Favorite Books - Pie Chart")
plt.axis('equal')  
plt.tight_layout()
plt.show()         


# Step 5: Line Graph
plt.figure()
plt.plot(books, ratings, marker='o', linestyle='-', color='blue')  # <<< Line Graph here
plt.title("Favorite Books and Their Ratings - Line Graph")
plt.xlabel("Books")
plt.ylabel("Ratings (1-10)")
plt.ylim(0, 10)
plt.xticks(rotation=45)
plt.grid(True)  # <<< Optional: Add grid lines
plt.tight_layout()
plt.show()

line, = ax2.plot([], [], marker='o', linestyle='-', color='blue')

# Define x positions
x_pos = np.arange(len(books))


def animate_line(frame):
    line.set_data(x_pos[:frame], ratings[:frame])
    ax2.set_xlim(-0.5, len(books)-0.5)
    return line,

ani_line = animation.FuncAnimation(fig2, animate_line, frames=len(books)+1, interval=500, blit=True) # type: ignore

plt.tight_layout()
plt.show()
