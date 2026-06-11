age=int(input("Enter your age: "))
if age>=18:
    print("Eligible for voting")
else:
    raise Exception("Not Eligible for voting")