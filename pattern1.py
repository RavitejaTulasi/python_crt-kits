n = int(input('Enter the integer: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*', end=" ")
    print()

#single loop
n=int(input('Enter the integer: '))
for i in range(1,n+1):
    print('*'*n)