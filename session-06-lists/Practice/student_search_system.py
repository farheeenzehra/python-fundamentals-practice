students = ["Farheen", "Hanna", "Naina", "Maha"]
name = input("Enter the student name you want to search: ")

if name in students:
    print("\nStudent found successfully!")
else:
    print("\nStudent not found!")

print("\nStudent List:")

for student in students:
    print(student)