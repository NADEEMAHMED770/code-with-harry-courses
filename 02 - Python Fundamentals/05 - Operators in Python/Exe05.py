username = input("Enter Username: ")
password = input("Enter Password: ")
saved_user = "admin"
saved_pass = "1234"

if (username==saved_user and password==saved_pass):
    print("Login SuccessFul")
elif (username==saved_user and password!=saved_pass):
    print("You Entered Incorrect Password")
elif (username!=saved_user and password==saved_pass):
    print("You Entered Incorrect UserName")
else:
    print("Incorrect UserName and Password")

