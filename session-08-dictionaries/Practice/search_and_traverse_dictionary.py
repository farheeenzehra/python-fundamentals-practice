student = {
    "name": "Farheen Zehra",
    "age": 21,
    "city": "Gilgit",
    "major": "BSAI",
    "gpa": 3.5
}

print("===== STUDENT INFORMATION =====")
for key in student:
    print(key + " : " + str(student[key]))
print()

search = input("Enter which information you want: ")
if search in student:
    print(search + " : " + str(student[search]))
else:
    print("Information not found!")