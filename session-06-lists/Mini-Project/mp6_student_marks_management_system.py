students = []
marks = []
quantity = int(input("Enter the number of students you want: "))

for i in range(quantity):
    student = input("Enter the name of the student: ")
    points = int(input("Enter marks of the student: "))
    students.append(student)
    marks.append(points)

print("======== STUDENT RECORD ========")
for i in range(quantity):
    print(students[i] + " : " + str(marks[i]))
print("=========================")

print("Total Students:", len(students))

name = input("Enter the name you want to search: ")
if name in students:
    print("Student found")
else:
    print("Student not found")

marks.sort()
print("Sorted Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))