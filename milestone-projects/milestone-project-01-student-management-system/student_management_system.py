def menu():
    print("====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Show Statistics")
    print("5. Exit")

    choice = int(input("Select an Option: "))
    return choice

choice = menu()

students = []

while choice != 5:
    
    if choice == 1:
        print("===== ADD STUDENT =====")
        name = input("Enter name of the student: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == 2:
        print("===== STUDENT LIST =====")
        if len(students) == 0:
            print("No students added yet.")
        else:
            for student in students:
                print(str(students.index(student) + 1) + ". " + student)

            print("Total Students: " + str(len(students)))

    elif choice == 3:
        print("===== SEARCH STUDENT =====")
        search = input("Enter the name you want to search: ")
        if search in students:
            print(search + " found successfully!")
        else:
            print(search + " not found!")

    elif choice == 4:
        print("===== STUDENT STATISTICS =====")
        if len(students) == 0:
            print("There are no students added currently.")
        else:
            print("Total Students: " + str(len(students)))
            print("First Student: " + students[0])
            print("Last Student: " + students[len(students) - 1])

    else:
        print("Invalid option selected.")

    print()
    choice = menu()

print("Thank you for using the Student Management System. Goodbye!")