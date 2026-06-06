size = int(input("Enter the size of list: "))
Age = []
for i in range(size):
    Age.append(int(input("Enter the age of person: ")))
print(Age)
for i in Age:
    if (i>=1 and i<=100):
        if(i<12):
            print(f"{i}-------> $10")
        elif(i>=12 and i<=60):
            print(f"{i}-------> $15")
        else:
            print(f"{i}-------> $12")