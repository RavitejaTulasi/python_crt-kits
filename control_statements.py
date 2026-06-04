# 1Q Write a python program to read age as input from the user and check whether  the age valid to vote or not. 
age = int(input("Enter your age: "))
if age >=18 :
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#ternary operator
age = int(input("Enter your age: "))
res= "eligible" if age>=18 else "not eligible"
print(f"You are {res} to vote")

# 2Q
a = int(input("Enter a number: "))
if a > 0:
    print(f"{a} is a positive number")
elif a<0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is zero")

r = "is positive number " if a > 0 else "is negative number" if a < 0 else "is zero"
print(f"{a} {r}")


# 3Q
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"The maximum of {num} and {num2} is {num if num >num2 else num2}")
print(f"The Minimum of {num} and {num2} is {num if num < num2 else num2}")

# 4Q
month = int(input("Enter month number: "))
if(month >=1 and month <=12):
    print(f"{month} is valid.")
else:
    print(f"{month} is invalid.")

# 5Q
month = int(input("Enter month number: "))
if month >= 1 and month <=12 :
    if month in [1,3,5,7,8,10,12]:
        print(f"{month} has 31 days.")
    elif month in [4,6,9,11]:
        print(f"{month} has 30 days.")
    elif month == 2:
        print(f"{month} has 28 or 29 days.")
else:
    print(f"{month} is invalid.")


# 6Q
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#7Q
year = int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0) :
	print(f"{year} is a leap year.")
else:
	print(f"{year} is not a leap year.")