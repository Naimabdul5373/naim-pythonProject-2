import matplotlib.pyplot as plt

# Data
genres = ['Fiction', 'Non-Fiction', 'Science', 'History']
sales = [200, 150, 300, 100]

# Check
if len(genres) != len(sales):
    print("Error: Genres and Sales must match in length!")
else:
    plt.bar(genres, sales)
    plt.title('Bookstore Sales by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Books Sold')
    plt.show()
