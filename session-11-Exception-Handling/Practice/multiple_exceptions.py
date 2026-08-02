try:
    num1 = input("Enter first number: ")
    num2 = int(input("Enter second number: "))
    print("Division:", int(num1) / num2)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")