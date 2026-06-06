def add(a,b):
    print(f"The Addition of {a} and {b} is {a+b}")
def subtract(a,b):
    print(f"The Subtraction of {a} and {b} is {a-b}")
def multiply(a,b):
    print(f"The Multiplication of {a} and {b} is {a*b}")
def division(a,b):
    if b!=0:
        print(f"The Division of {a} and {b} is {a/b}")
    else:
        print("Division by zero is not allowed.")
def rem(a,b):
    if b!=0:
        print(f"The Remainder of {a} and {b} is {a%b}")
    else:
        print("Division by zero is not allowed.")
while True:
    print("The Choices you have are: ")
    print("--------------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exit")
    print("--------------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        print("Exit")
        print("--------------------------------------")
        break
    if choice<1 or choice>6:
        print("Invalid Choice, try again.")
        print("--------------------------------------")
        continue
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if choice ==1:
        add(a,b)
    elif choice==2:
        subtract(a,b)
    elif choice==3:
        multiply(a,b)
    elif choice==4:
        division(a,b)
    elif choice==5:
        rem(a,b)
print("\n")