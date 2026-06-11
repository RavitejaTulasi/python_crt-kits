balance =5000

try:
    amount = int(input("Enter withdrawal amount : "))
    if amount > balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawal Successful")

except ValueError as e:
    print("Transaction Failed", e)

print("\n")

try:
    monthly_salary = int(input("Enter your monthly salary: "))
    if monthly_salary<=0:
        raise ValueError
    annual_salary = monthly_salary *12
    print("Annual Salary:",annual_salary)
except ValueError:
    print("Please enter a valid salary amount.")


pin= input("Enter the Password: ")
try:
    if(pin=="1234"):
        print("LOgin is successful")
    else:
        raise TypeError("Incorrect Password")
except TypeError as e:
    print(e)


a=10
try:
    print(a)
finally:
    print('Finally Block Code')