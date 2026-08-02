def features():
    print("====== SAFE CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    option = int(input("Select the option you want: "))
    return option

option = features()

while option != 5:
    if option == 1:
        print("===== ADDITION =====")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif option == 2:
        print("===== SUBTRACTION =====")
        try:
            num1= float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif option == 3:
        print("===== MULTIPLICATION =====")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif option == 4:
        print("===== DIVISION =====")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
            print("Result:", result)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except ZeroDivisionError:
            print("Error! Division by zero is not allowed.")
            
    else:
        print("Invalid Option Selected!")
    
    option = features()

print("Exiting Safe Calculator...")