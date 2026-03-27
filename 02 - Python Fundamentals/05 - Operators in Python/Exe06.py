price = float(input("Enter Price Per Item: "))
quantity = int(input("Enter Quantity: "))
user_type = input("Enter you user type (student or regular): ")
counted_price = price*quantity
if (user_type=="student"):
    if (counted_price<5000):
        discount_price = counted_price*0.10
        final_price = counted_price-discount_price
        print("Original Price: ",counted_price)
        print("Student Discount Applied: 10%")
        print("Final Price: ",final_price)
    else:
        discount_price = counted_price*0.15
        final_price = counted_price-discount_price
        print("Original Price: ",counted_price)
        print("Student Discount Applied: 10%")
        print("Extra Discount Applied: 5%")
        print("Final Price: ",final_price)
elif (user_type=="regular"):
    if (counted_price<5000):
        discount_price = counted_price*0.05
        final_price = counted_price-discount_price
        print("Original Price: ",counted_price)
        print("Discount Applied: 5%")
        print("Final Price: ",final_price)
    else:
        print("Original Price: ",counted_price)
        print("No Discount Applied")
        print("Final Price: ",counted_price)
else:
    print("Invalid User Type")
