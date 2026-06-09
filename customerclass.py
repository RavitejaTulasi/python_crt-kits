class Customer:
    def __init__(self):
        pass
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_id(self,id):
        self.id=id

    def get_name(self):
        print(f"name is: {self.name}")
    def get_id(self):
        print(f"id is: {self.id}")
    def get_age(self):
        print(f"age is: {self.age}")

s1=Customer()
s1.set_name("Ravi")
s1.set_id("23jr")
s1.set_age(20)
s1.get_name()
s1.get_id()
s1.get_age()