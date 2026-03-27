age = int(input("Enter your age: "))
nationality = input("Enter your Nationality: ")

if (age>=18 and nationality=="pakistani" or nationality=="Pakistani" or nationality=="PAKISTANI"):
    print("You are Eligible.")
else:
    print("You are not Eligible.")