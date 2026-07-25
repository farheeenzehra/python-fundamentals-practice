print("WELCOME TO THE STUDENT PERCENTAGE CALCULATOR")

student_name = input("Enter your name: ")
english_marks = int(input("Enter your marks in English: "))
maths_marks = int(input("Enter your marks in Maths: "))
science_marks = int(input("Enter your marks in Science: "))

total_marks = english_marks + maths_marks + science_marks
max_marks = 300
percentage = total_marks / max_marks * 100

print("\n========== RESULT ==========")
print("Name:", student_name)
print("English:", english_marks)
print("Maths:", maths_marks)
print("Science:", science_marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
print("============================")