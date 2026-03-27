marks = int(input("Enter your marks: "))

if (marks>100 or marks<0):
    print("Invalid Marks")
elif (marks>=85):
    print("A Grade")
elif (marks>=70):
    print("B Grade")
elif (marks>=50):
    print("C Grade")
else:
    print("FAIL")