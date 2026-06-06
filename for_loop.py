#1Q
for i in range(1,6):
    print("Hello world")

#2Q
num = int(input("Enter a natural number: "))
for i in range(1,num+1):
    print(i)

#3Q
num=int(input("Enter a natural number: "))
for i in range(num,0,-1):
    print(i)


#4Q
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2==0):
        print(i)

for i in range(2,n+1,2):
    print(i)



#5Q
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%2!=0):
        print(i)

for i in range(1,n+1,2):
    print(i)


#6Q
sum=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    sum=sum+i
print(f"sum of first {n} numbers is {sum}")

#7Q
fact=1
n=int(input("Enter a number: "))
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial of {n} is: {fact}")


#8Q
n = int(input("Enter a number: "))
print(f"Multiplication table of {n} is:")
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


#9Q
n = int(input("Enter a number: "))
print(f"Multiplication table of {n} is:")
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")

#11Q
#down to up multiplication tables
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    print(f"Multiplication table of {i} is:")
    print("-"*20)
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

#10Q
#sup to down multiplication tables
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(f"Multiplication table of {i} is:")
    print("-"*40)
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")


#12Q
# reverse order of multiplication tables
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(f"Multiplication table of {i} is:")
    print("-"*20)
    for j in range(10,0,-1):
        print(f"{i} X {j} = {i*j}")


