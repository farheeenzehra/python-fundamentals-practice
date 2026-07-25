def welcome():
    print("WELCOME TO THE SIMPLE CALCULATOR")

def calculate():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    total = number1 + number2
    
    print("Sum:", total)

def goodbye():
    print("Thank you for using the calculator.")

welcome()
calculate()
goodbye()