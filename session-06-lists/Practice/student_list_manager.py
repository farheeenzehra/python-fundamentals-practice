students = ["Ahmed", "Farheen", "Ayesha"]

print("Original Student List:")
print(students)

students.append("Ali")
students.insert(2, "Sara")
students.remove("Ahmed")

if "Sara" in students:
    students[students.index("Sara")] = "Sarah"
print("\nUpdated Student List:")
print(students)