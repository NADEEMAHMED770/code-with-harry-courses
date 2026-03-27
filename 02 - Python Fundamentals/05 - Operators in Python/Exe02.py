num1 = int(input("Enter a number: "))
if (num1>0 and num1%2==0):
    print("Positive Even Number")
elif (num1>0 and num1%2!=0):
    print("Positive Odd Number")
elif (num1<0 and num1%2==0):
    print("Negative Even Number")
elif (num1<0 and num1%2!=0):
    print("Negative Odd Number")
else:
    print("Number is Zero")