class Mobile:
    def __init__(self,brand,price,color):
        print("Mobile object is created...!")
        self.brand=brand
        self.price=price
        self.color=color
def Details(self):
    print(f"Brand is: {self.brand}")
    print(f"price is: {self.price}")
    print(f"color is: {self.color}")
    print("-"*40)
m1=Mobile("Redmi",20000,"Red")
Details(m1)
m2=Mobile("Realme",18000,"blue")
Details(m2)
m3=Mobile("samsung",30000,"grey")
Details(m3)
m4=Mobile("oneplus",25000,"Dark blue")
Details(m4)
m5=Mobile("Iphone",150000,"white")
Details(m5)
