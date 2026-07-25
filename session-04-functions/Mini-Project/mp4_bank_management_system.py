balance = 5000

def welcome():
    print("WELCOME TO ABC BANK")

def deposit():
    global balance
    deposit_amount = int(input("Enter the amount to deposit: "))
    balance += deposit_amount

    print("Deposit Successful!")
    print("Current Balance:", balance)

def check_balance():
    print("Your Current Balance is:", balance)

def goodbye():
    print("Thank you for banking with us!")
    print("Have a great day!")

welcome()
check_balance()
deposit()
check_balance()
goodbye()