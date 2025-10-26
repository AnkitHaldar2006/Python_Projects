correct_password = "RTX 3060 Ti"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.\n")
