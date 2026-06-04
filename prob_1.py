bill_amount = int(input("Enter the bill amount: "))
if bill_amount > 500:
    discount = bill_amount * 0.1
    final_amount = bill_amount - discount
    print(f"You got a discount of {discount}. Your final bill amount is {final_amount}.")
else: 
    print(f"Your bill amount is {bill_amount}. No discount applied.")