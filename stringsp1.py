Str = "                 python proGram on strinG functions"
print(Str.capitalize())
print(Str.casefold())
print(Str.center(100,"*"))
print(Str.count('user'))
print(Str.encode())
print(Str.endswith('.'))
print(Str.expandtabs(4))


'''
ord()-- converts any character into ascii value
chr()-- converts ascii value into character
'''

for ch in range(ord('A'),ord('Z')+1):
    print(chr(ch))