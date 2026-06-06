#scott@oracle.in
Str="scott@oracle.in"
a=Str.find('@')
d=Str.find('.')
print("employee name is: ",Str[0:a])
print("company name is: ",Str[a+1:d])