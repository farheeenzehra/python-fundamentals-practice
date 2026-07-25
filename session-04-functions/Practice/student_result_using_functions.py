def greeting():
    print("WELCOME TO THE STUDENT RESULT SYSTEM")


def result():
    name = input("Enter your name: ")
    marks_english = int(input("Enter your marks in English: "))
    marks_math = int(input("Enter your marks in Maths: "))
    marks_science = int(input("Enter your marks in Science: "))

    total_marks = marks_english + marks_math + marks_science
    percentage = (total_marks / 300) * 100

    print("\n========== RESULT ==========")
    print("Name:", name)
    print("Total Marks:", total_marks)
    print("Percentage:", round(percentage, 2), "%")


greeting()
result()