total=0
while True:
    size = input("Enter the size of the pizza: ").lower()
    if size == "small":
        total=total+10
    elif size == "medium":
        total = total+15
    elif size == "large":
        total = total+20
    else:
        print("choose a size")
        continue
    no_toppings=int(input("Enter the number of toppings: "))
    for i in range(no_toppings):
        toppings=input("Enter your topping: ").lower()
        if toppings=="olives":
            total = total+5
        elif toppings=="cheese":
            total = total+2
        elif toppings=="pepperoni":
            total = total+3
        elif toppings=="Jalapenos":
            total=total+5
    print(f"Your total bill is: ${total}")
    print("Thank you for visting.")
print("\n")




