# Student List Program

# Create an empty list to store student names
students = []

# Ask user to enter 3 student names
for i in range(512):
    name = input("Enter a student name: ")
    students.append(name)

# Display the list of students
print("\nHere are the students:")
print(students)

# Ask if the user wants to remove a name
choice = input("\nWould you like to remove a name? (yes or no): ").lower()

if choice == "yes":
    name_to_remove = input("Which name would you like to remove?: ")
    if name_to_remove in students:
        students.remove(name_to_remove)
        print("\nHere is the updated list:")
        print(students)
    else:
        print("\nThat name was not found in the list.")
else:
    print("\nNo changes made to the list.")

