import numpy as np

Zero=np.array(10)
print(Zero)
print(type(Zero))
print("Dimension :",Zero.ndim)
print("Memory :",Zero.nbytes)

#one Dimensional array
One=np.array([12,24,36,49,60])
print(One)
print(type(One))
print("Dimension :",One.ndim)
print("Memory :",One.nbytes)

#two Dimensional array
Two=np.array([[12,24,36,39],[49,60,72,84]])
print(Two)
print(type(Two))
print("Dimension :",Two.ndim)
print("Memory :",Two.nbytes)

#three Dimensional array
three=np.array([[[12,24,36,39],[49,60,72,84]],[[13,25,37,40],[50,61,73,85]]])
print(three)
print(type(three))
print("Dimension :",three.ndim)
print("Memory :",three.nbytes)


print("\n")
a=np.array([1,2,3,4,5])
print(a)
z=np.zeros(5)
print(z)
o=np.ones((2,3))
print(o)
r=np.arange(0,10,2)
print(r)
l=np.linspace(0,1,5)
print(l)
rd=np.random.randint(1,100,6)
print(rd)

print("\n")

#vectorized maths
g=np.array([1,2,3,4,5])
g + 10
g * 2
c=np.sqrt(g)
d=np.square(g)
e=np.clip(g,2,4)
print(c)
print(d)
print(e)

print("\n")

p1=np.mean(g)
p2=np.median(g)
p3=np.std(g)
p4=np.percentile(g,25)
print(p1)
print(p2)
print(p3)
print(p4)

print("\n")
#shape/reshape
print(g.reshape(5,1))
print(g.shape)
print(g.dtype)
print(g.astype(float))

print("\n")
