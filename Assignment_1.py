#1Q
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if (num1>num2 and num1>num3):
    print(f"{num1} is the greatest number")
elif (num2>num3):
    print(f"{num2}is the greatest number")
else:
    print(f"{num3} is the greatest number.")

#2Q
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if (num1<num2 and num1<num3):
    print(f"{num1} is the smallest number")
elif (num2<num3):
    print(f"{num2} is the smallest number")
else:
    print(f"{num3} is the smallest number")

#3Q
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
if (num1<num2):
    print(f"{num1} is the smallest number")
else:
    print(f"{num2} is the smallest number")

# 4Q
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
if (num1 == num2 and num1 == num3):
    print("All numbers are equal")
else:
    if (num1>num2 and num1<num3):
        print(f"{num1} is the middle number")
    elif (num2>num1 and num2<num3):
        print(f"{num2} is the middle number")
    else:
        print(f"{num3} is the middle number")