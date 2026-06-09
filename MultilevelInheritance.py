class A:
    def __init__(self, name):
        self.name = name
class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
class c(B):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender

s1=c('sachin',20,'male')
print(s1.age)