class A:
    def __init__(self, a):
        self.a = a
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b=b
class C(A):
    def __init__(self,a,c):
        super().__init__(a)
        self.c=c

s1=B(10,20)
s2=C(10,30)
print(s1.a)
print(s1.b)
print(s2.a)
print(s2.c)