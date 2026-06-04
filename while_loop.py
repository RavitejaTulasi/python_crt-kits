#1Q
num = int(input("Enter a natural number: "))
i=1
while (i<=num):
    print(i)
    i+=1 #i=i+1

#2Q continue and break
for i in range(1,11):
    if i==5:
        continue #skip the rest of the code and move to the next iteration
    print(i)

for i in range(1,11):
    if i==5:
        break #exit the loop
    print(i)


#3Q
n=5
for i in range(1,11):
    m=n*i
    if m%2!=0:
        continue
    print(f"{n} x {i} = {m}")


#4Q
num = int(input("Enter a natural number: "))
count = 0
rem = 0
while num!=0:
    rem = num%10
    count+=1
    num = num//10
print(f"The count of digits in the given number is {count}.")

#5Q
num = int(input("Enter a natural number: "))
sum = 0
rem = 0
while num!=0:
    rem = num%10
    sum+=rem
    num = num//10
print(f"The sum of digits in the given number is {sum}.")






