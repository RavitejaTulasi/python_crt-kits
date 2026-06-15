n=int(input('Enter the integer: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print()

print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64),end=' ')
    print()

print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+96),end=' ')
    print()
print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64),end=' ')
    print()

print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+96),end=' ')
    print()
print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i % 2 == 0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()

print('-'*65)

for i in range(1,n+1):
    for j in range(1,n+1):
        if j % 2 == 0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()