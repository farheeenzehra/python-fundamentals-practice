try:
    number = input("Enter a number: ")
    number = int(number)
    print("You entered the number: " + str(number))

except ValueError:
    print("Invalid input. Please enter a valid integer.")