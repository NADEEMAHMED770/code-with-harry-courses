allowed_users = ["admin", "manager", "editor","student"]
user_name = input("Enter your username: ")
if user_name in allowed_users:
    print("Access Granted")
elif user_name not in allowed_users:
    print("Access Not Granted")
else:
    print("User Name Cannot be Empty")