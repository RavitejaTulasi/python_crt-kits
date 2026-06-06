pizzas=int(input("Enter the number of pizzas you want to order: "))
total=0
for i in range(pizzas):
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
            elif toppings=="jalapenos":
                total=total+5
            else:
                print("NO topping added")
        if total<50 and total>0:
            total+=5
        elif total>50:
            pass
print(f"Your total bill is: ${total}")
if total>50:
    print("free delivery")
print("Thank you for visting.")
print("\n")




