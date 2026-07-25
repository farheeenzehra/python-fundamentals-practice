def welcome():
    print("WELCOME TO ABC BANK")

def check_balance():
    name = input("Enter your name: ")
    account_balance = int(input("Enter your account balance: "))

    print("\nName:", name)
    print("Account Balance:", account_balance)

    if account_balance >= 5000:
        print("Status: Premium Customer")
    else:
        print("Status: Regular Customer")

def goodbye():
    print("\nThank you for banking with us. Have a nice day!")

welcome()
check_balance()
goodbye()