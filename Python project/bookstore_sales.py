import matplotlib.pyplot as plt

# Define your genres and sales
genres = ['Fiction', 'Non-Fiction', 'Science', 'History']
sales = [200, 150, 300, 100]

# Check if lengths match
if len(genres) != len(sales):
    print("Mismatch between genres and sales data!")
else:
    # Create the bar graph
    plt.bar(genres, sales)

    # Add title and labels
    plt.title('Bookstore Sales')
    plt.xlabel('Genre')
    plt.ylabel('Sales')

    # Show the plot
    plt.show()
