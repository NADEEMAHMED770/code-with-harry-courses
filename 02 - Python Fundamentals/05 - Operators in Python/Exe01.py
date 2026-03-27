num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1+num2
difference = num2-num1
product = num1*num2
division = num1/num2

print("Sum: ",sum)
print("Difference: ",difference)
print("Product: ",product)
print("Division: ",division)

if (num1>num2):
    print(num1," is greater.")
elif (num1<num2):
    print(num2, " is greater.")
else:
    print(num1," is equals to ",num2)
