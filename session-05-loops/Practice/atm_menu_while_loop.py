print("WELCOME TO ABC BANK")
choice = 0
while choice != 3:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance: 5000")
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        print("Deposit Successful!")
    elif choice == 3:
        print("Thank you for using ABC Bank!")
    else:
        print("Invalid Choice!")