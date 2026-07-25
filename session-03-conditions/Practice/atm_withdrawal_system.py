print("WELCOME TO THE ATM")
name = input("Enter your name: ")
account_balance = int(input("Enter your account balance: "))
withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

if withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount

    print("\nTransaction Successful!")
    print("Remaining Balance:", remaining_balance)
else:
    print("\nInsufficient Funds!")