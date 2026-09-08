username = "python"
password = "rules"

usernameEntered = input("Enter username: ")
passwordEntered = input("Enter password: ")

guessNumber = 1

while guessNumber !=5:
    if usernameEntered == username and passwordEntered == password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        guessNumber += 1
        usernameEntered = input("Enter username: ")
        passwordEntered = input("Enter password: ")
else:
    print("Access denied")