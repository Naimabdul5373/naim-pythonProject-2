import matplotlib.pyplot as plt

# Data
genres = ['Fiction', 'Non-Fiction', 'Science', 'History']
sales = [200, 150, 300, 100]

# Create Figure and Size
plt.figure(figsize=(8,6))

# Professional Bar Chart
bars = plt.bar(genres, sales, edgecolor='black', linewidth=1.5)

# Add colors
for bar in bars:
    bar.set_color('skyblue')

# Titles and Labels
plt.title('📚 Bookstore Sales by Genre', fontsize=18, fontweight='bold')
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Sales', fontsize=14)

# Gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show Chart
plt.tight_layout()
plt.show()
