import matplotlib.pyplot as plt

# Data
genres = ['Fiction', 'Non-Fiction', 'Science', 'History']
sales = [200, 150, 300, 100]

# Create Figure and Size
plt.figure(figsize=(8,8))

# Professional Pie Chart
explode = (0, 0.1, 0, 0)  # Only 'explode' Non-Fiction slice
colors = ['lightcoral', 'lightskyblue', 'yellowgreen', 'gold']

plt.pie(sales, labels=genres, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Title
plt.title('🥧 Bookstore Sales Distribution', fontsize=18, fontweight='bold')

# Equal aspect ratio ensures pie is a circle
plt.axis('equal')

# Show Chart
plt.tight_layout()
plt.show()


