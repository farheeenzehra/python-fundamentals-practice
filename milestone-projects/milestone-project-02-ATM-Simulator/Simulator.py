history = []

accounts = {
    "Farheen": {
        "pin": 1234,
        "balance": 1000
    },

    "Ali": {
        "pin": 5678,
        "balance": 500
    }
}

current_user = ""


# Verify user

def verify_pin():

    global current_user

    attempts = 0

    while attempts < 5:

        username = input("Enter your username: ")

        try:
            pin = int(input("Enter your PIN: "))

        except ValueError:
            print("PIN should be a number.")
            continue

        if username in accounts:

            if accounts[username]["pin"] == pin:
                current_user = username
                print("Login successful.")
                return True

            else:
                attempts += 1
                print("Incorrect PIN.")
                print("Attempts left:", 5 - attempts)

        else:
            print("User not found.")
            return False

    print("Too many wrong attempts.")
    return False


# Show menu

def menu():

    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")

    while True:

        try:
            option = int(input("Choose an option: "))

            if option in [1, 2, 3, 4, 5, 6]:
                return option

            print("Choose a valid option.")

        except ValueError:
            print("Enter a number.")


# Print receipt

def print_receipt(transaction, amount):

    print("\nReceipt")
    print("User:", current_user)
    print("Transaction:", transaction)
    print("Amount:", amount)
    print("Balance:", accounts[current_user]["balance"])


# Check balance

def check_balance():

    print("Current Balance:", accounts[current_user]["balance"])


# Deposit money

def deposit_money():

    deposit = float(input("Enter amount to deposit: "))

    if deposit > 0:

        accounts[current_user]["balance"] += deposit

        history.append(
            current_user +
            " deposited " +
            str(deposit)
        )

        print("Money deposited successfully.")

        print_receipt("Deposit", deposit)

    else:
        print("Enter a valid amount.")


# Withdraw money

def withdraw_money():

    withdraw = float(input("Enter amount to withdraw: "))

    if withdraw <= 0:

        print("Enter a valid amount.")

    elif withdraw > accounts[current_user]["balance"]:

        print("Insufficient balance.")

    else:

        accounts[current_user]["balance"] -= withdraw

        history.append(
            current_user +
            " withdrew " +
            str(withdraw)
        )

        print("Money withdrawn successfully.")

        print_receipt("Withdrawal", withdraw)


# Show history

def show_history():

    print("\nTransaction History")

    if history:

        for transaction in history:
            print(transaction)

    else:
        print("No transactions yet.")


# Change PIN

def change_pin():

    old_pin = int(input("Enter current PIN: "))

    if old_pin == accounts[current_user]["pin"]:

        new_pin = int(input("Enter new PIN: "))

        accounts[current_user]["pin"] = new_pin

        print("PIN changed successfully.")

    else:

        print("Incorrect current PIN.")


# Start ATM

print("Welcome to the ATM!")

if verify_pin():

    while True:

        option = menu()

        if option == 1:
            check_balance()

        elif option == 2:
            deposit_money()

        elif option == 3:
            withdraw_money()

        elif option == 4:
            show_history()

        elif option == 5:
            change_pin()

        elif option == 6:
            print("Thank you for using our ATM.")
            print("Goodbye!")
            break