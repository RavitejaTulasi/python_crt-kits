Lang = {
    'UI/UX':['HTML', 'CSS', 'JavaScript','React js', 'Express js'],
    'Backend':['python','Flask','Django','pyramid','Bottle'],
    'server':['Sql','pl-sql','Ms-sql']
}
print(Lang['UI/UX'])
print(Lang['Backend'])
print(Lang['server'])
Lang['server']=['oracle sql']
print(Lang['server'])

print('\n')

std = {
    101:'scott',102:'miller',103:'adams',104:'james',105:'david'
}
print(std)
std[106]='xyz'
print(std)
del std[101]
del std[106]
print(std)
#check 101,104,105
print(101 in std)
print(104 in std)
print(105 in std)
print('\n')
print(std.clear())

print('\n')

print(Lang.values())
print(Lang.keys())
print(Lang.items())
print('\n')

colors={}
keys=(101,102,103)
values='red'
print(colors.fromkeys(keys,values))
print('\n')

stdd={
    101:'scott',102:'miller',103:'adams',104:'james',105:'david'
}
print(stdd.get(101))
print(stdd.get(105))
print(stdd.items())
stdd.update({105:'Gupchup'})
print(stdd)
stdd.pop(101)
print(stdd)
print(stdd.popitem())
print(stdd)

stdd.setdefault(107,'Null')
print(stdd)
print('\n')

#nested dictionary
dict={
    'std1':(101,'scott',20),
    'std2':(102,'miller',23)
}
for i in dict:
    print(i,dict[i])