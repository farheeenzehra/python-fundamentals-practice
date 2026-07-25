print("WELCOME TO THE GRADE CALCULATOR")
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)