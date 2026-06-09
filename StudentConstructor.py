class Student:
    def __init__(self,name,age):
        print("Student object is created...!")
        self.name=name
        self.age=age
def Details(self):
    print("-"*50)
    print(f"name is: {self.name}")
    print(f"age is: {self.age}")
s1=Student("Ravi",20)
Details(s1)
s2=Student("Teja",20)
Details(s2)
s3=Student("vijay",20)
Details(s3)
s4=Student("Sai",20)
Details(s4)
s5=Student("shiva",20)
Details(s5)