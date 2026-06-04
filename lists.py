cartoons = ["Tom and jerry", 'Doraemon', 'Shinchan', 'Chhota Bheem', 'Motu Patlu']

print('Accessing using positive indexing')
print(cartoons[0])
print(cartoons[1])
print(cartoons[2])
print(cartoons[3])
print(cartoons[4])

print('Accessing using negative indexing')
print(cartoons[-1])
print(cartoons[-2])
print(cartoons[-3])
print(cartoons[-4])
print(cartoons[-5])


cartoons = ["Tom and jerry", 'Doraemon', 'Shinchan', 'Chhota Bheem', 'Motu Patlu']
for i in range(len(cartoons)):
    print(f"Cartoon at index {i} is {cartoons[i]}")
#without using index
for i in cartoons:
    print(i)


# using while loop
cartoons = ["Tom and jerry", 'Doraemon', 'Shinchan', 'Chhota Bheem', 'Motu Patlu']
i=0
while i<len(cartoons):
    print(cartoons[i])
    i+=1


cartoons = ["Tom and jerry", 'Doraemon', 'Shinchan', 'Chhota Bheem', 'Motu Patlu']
print(cartoons)
del cartoons[2]
print(cartoons)
del cartoons
print(cartoons)


List = [5,10,2,4,15,6,8,12,20,3]
print(List)
print(len(List))
print(max(List))
print(min(List))
print(sum(List))
print(sorted(List))
print(sum(List)/len(List))



''' List Slicing - Extracting a portion of the list.
[start:stop:step]
default values:
start = 0
stop = len(list)
step = 1
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(my_list[:])
print(my_list[0:5])
print(my_list[::2])
print(my_list[5:])
print(my_list[-6:-2])
print(my_list[::-1])


List = ['python', 'java', 'c++', 'javascript']
print(List)
List.append('ruby')
print(List)
List.append('Sql')
print(List)

list = ['python', 'java', 'c++', 'javascript']
print(list)
list.insert(0, 'SQL')
list.insert(2, 'C programming')
list.insert(3,'javascript')
list.insert(1, 'ruby')
print(list)
print('\n')

list.pop()
print(list)
list.pop(3)
print(list)
list.remove('c++')
print(list)
print(list.index('java'))
print(list.index('javascript'))
list.reverse()
print(list)
print('\n')

frontend = ['html', 'css', 'javascript','Bootstrap','Reactjs']
lang = ['python', 'Django', 'Flask', 'Nodejs, Expressjs']
print(frontend)
print(lang)
lang.extend(frontend)
print(lang)
print('\n')

li = [1,3,1,5,1,4,7]
print(li.count(1))
li.sort()
print(li)
li.reverse()
print(li)
lt = li
lt.clear()
print(lt)
print(li)

li =[10,20,30]
lt=[1,2,3]
a=li+lt
print(a)

b=[1,2,3]
r=b*3
print(r)


#shallow  copy
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a)
print(b)
b=a
print(b)
a.append(11)
print(b)
print(a)

#deep copy
import copy
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a)
print(b)
b=copy.deepcopy(a)
print(b)
a.append(11)
print(b)
print(a)



a=[1,2,35,6,8,6,5,8,99,0,66]
print(a)
a.append(5)
print(a)
a.insert(2,85)
print(a)
a.remove(2)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
print(a.index(85))
print(a.count(2))
print(a.sort())
print(a.reverse())
print(a[:5])



