student = {
    "name": "Farheen Zehra",
    "age": 21,
    "city": "Gilgit",
    "major": "BSAI",
    "gpa": 3.5
}

def menu():
    print("===== STUDENT PROFILE MANAGEMENT SYSTEM =====")
    print("1. Display Profile")
    print("2. Search Information")
    print("3. Update Information")
    print("4. Remove Information")
    print("5. Exit")

    option = int(input("Select an Option: "))
    return option

option = menu()

while option != 5:
    
    if option == 1:
        print("===== STUDENT PROFILE =====")
        for key in student:
            print(key + " : " + str(student[key]))

    elif option == 2:
        print("===== SEARCH INFORMATION =====")
        search = input("Enter the key you want to search: ")

        if search in student:
            print(search + " : " + str(student[search]))
        else:
            print(search + " Not Found!")

    elif option == 3:
        print("===== UPDATE INFORMATION =====")
        update = input("Enter the key you want to update: ")

        if update in student:
            print(update + " Found Successfully!")

            new_value = input("Enter the new value: ")

            student[update] = new_value

            print(update + " Updated Successfully!")

        else:
            print(update + " Not Found!")

    elif option == 4:
        print("===== REMOVE INFORMATION =====")
        remove = input("Enter the key you want to remove: ")

        if remove in student:
            del student[remove]
            print(remove + " Removed Successfully!")
        else:
            print(remove + " Not Found!")

    else:
        print("Invalid Option Selected!")

    option = menu()

print("Exiting...")
print("Thank You!")