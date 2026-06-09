class Product:
    def __init__(self,name,price):
        print("Product object is created.....!")
        self.name=name
        self.price=price
        print("-"*40)
p1=Product("Phone",2000)
print(f"name: {p1.name}")
print(f"price: {p1.price}")
p2=Product("Laptop",100000)
print(f"name: {p2.name}")
print(f"price: {p2.price}")
p3=Product("Water Bottle", 50)
print(f"name: {p3.name}")
print(f"price: {p3.price}")
p4=Product("TextBook",100)
print(f"name: {p4.name}")
print(f"price: {p4.price}")
p5=Product("Charger", 500)
print(f"name: {p5.name}")
print(f"price: {p5.price}")




