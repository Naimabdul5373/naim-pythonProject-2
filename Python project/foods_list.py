food_lists = []  


for i in range(120):
    food = input("Enter a favorite food: ")
food_lists.append(food)

print("\nHere are your favorite foods:")
for food in food_lists: 
    print(f"- {food}")

