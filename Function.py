def greet():
    print("Hello, welcome to the demo!")
greet()
greet()
greet()


def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
add(10,20)
add(5,7)

def add(a,b):
    return a+b
print(add(10,20))
print(add(5,7))


#nested function
def one():
    def two():
        print("Two")
    print("One")
one()

#nested function calling
def washhands():
    print("Washing hands")
def servefood():
    print("Serving food")
def eatfood():
    washhands()
    servefood()
    print("Eating food")
    washhands()
eatfood()

#giving function as an argument to another function
def one(xyz):
    print("first function " + xyz())
def two():
    return "second function"
one(two)

#lambda function
add = lambda a, b : a + b
print(add(10,20))