#example for numeric type
a = 10
print(a)
print(type(a))
a = 3.14
print(f'a = {a}')
print(type(a))
a = 5+3j
print('a =', a)
print(type(a))


#sequence type - string, list, tuple, range

Lang=['java', 'python', 'c++', 'c']
print(Lang)
print(type(Lang))

lang = ('java', 'python', 'c++', 'c')
print(lang)
print(type(lang))

lang = {'java', 'python', 'c++', 'c'}
print(lang)
print(type(lang))


#string
str1 = 'Good Afternoon'
print(str1)
print(type(str1))
str2 = "I'm learning python"
print(str2)
print(type(str2))
str3 = '''Hi
Good Afternoon, everyone
we started with datatype
'''
print(str3)
print(type(str3))


#dictionary
lang = {101:{103:'java', 104:'c++'}, 102:'python'}
print(lang[101][103], lang[102])

#boolean
a = True
print(a)
print(type(a))

print(True + True)

#range
r = range(1, 10, 2)
print(r)
print(type(r))
for i in r:
    print(i)