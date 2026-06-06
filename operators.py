x=10
y=3
print(f"Addition of x & y is {x+y}")
print(f"Substraction of x & y is {x-y}")
print(f"Multiplication of x & y is {x*y}")
print(f"Division of x & y is {x/y}")
print(f"Module Division  of x & y is {x%y}")
print(f"positive floor Division x & y is{x//y}")



# relational operators 
print(10>25)
print(10<5)
print(10<=5)
print(10>=5)
print(10==10)
print(190!=5)

# assignment operators 
num=10
print(f"num = {num}")
num+=2
print(f"num = {num}")
num-=4
print(f"num = {num}")
num*=3
print(f"num = {num}")
num/=4
print(f"num = {num}")
num%=2



#bitwise operators
a=10
b=15
print(f"a & b = {a & b}")
print(f"a | b = {a | b}")
print(f"a ^ b = {a ^ b}")
print(f"~a = {~a}")
print(f"a << 2 = {a << 2}")
print(f"a >> 2 = {a >> 2}")

#membership operators
List = [10, 20 , 30 ,25 ,40, 15]
print(10 in List)#True
print(50 in List)#False
print(10 not in List)#False
print(50 not in List)#True
print("python" in "I am working on python")#True
print("python" not in "I am working on python")#False


#identity operators
num1=10
print(num1)
print(id(num1))
num2=10
print(num2) 
print(id(num2))
print(num1 is num2) #True
print(num1 is not num2) #False