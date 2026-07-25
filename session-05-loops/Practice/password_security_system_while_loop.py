print("WELCOME TO THE PASSWORD SECURITY SYSTEM")
correct_password = "fariii"
password = input("Enter your password: ")

while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter your password: ")

print("Password correct!")
print("Access granted.")