print("WELCOME! ADD YOUR DETAILS AND MARKS TO GET YOUR RESULT")
name = input ("enter your name  : ")
marks_english = input ("enter your marks in English : ")
marks_maths = input ("enter your marks in Maths : ")
marks_science =input ("enter your marks in Science : ")
marks_history = input ("enter your marks in History : ")
marks_geography = input ("enter your marks in Geography : ")
total_marks = int(marks_english) + int(marks_maths) + int(marks_science) + int(marks_history) + int(marks_geography)
max_marks = 500
percentage = total_marks / max_marks * 100
print("=========== YOUR RESULT ==========")
print("Name : " + name + "\n English : " + marks_english + "\n Maths : " + marks_maths + "\n Science : " + marks_science + "\n History : " + marks_history + "\n Geography : " + marks_geography + "\n Total Marks :  " + str(total_marks) + "\nPercentage : " + str(percentage))
print("Total Marks : " + str(total_marks) + "\nPercentage : " + str(percentage))