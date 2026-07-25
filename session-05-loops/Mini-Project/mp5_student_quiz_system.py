print("WELCOME TO THE STUDENT QUIZ SYSTEM")
correct_password = "fariii"
password = input("Enter the password: ")

while password != correct_password:
    print("Incorrect password! Please try again.")
    password = input("Enter the password: ")

print("\nLogin Successful!")
print("Let's begin the quiz.")

score = 0
for i in range(5):
    answer = input("Question " + str(i + 1) + ": What is the capital of Pakistan? ")

    if answer.lower() == "islamabad":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is Islamabad.\n")

print("========== QUIZ RESULT ==========")
print("Correct Answers:", score)
print("Wrong Answers:", 5 - score)
print("=================================")