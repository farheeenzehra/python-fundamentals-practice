print("WELCOME TO THE UNIVERSITY ADMISSION CHECKER")
student_name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))

print("\n========== ADMISSION RESULT ==========")
print("Student Name:", student_name)
print("Age:", age)
print("Percentage:", percentage)

if age >= 17 and percentage >= 60:
    print("Status: Congratulations! You are eligible for admission.")
else:
    print("Status: Sorry! You are not eligible for admission.")
print("======================================")