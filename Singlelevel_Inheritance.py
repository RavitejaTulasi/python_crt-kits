class Vechile:
    def __init__(self,brand,price,color,seating):
        self.brand=brand
        self.price=price
        self.color=color
        self.Seating=seating

class Bike(Vechile):
    def __init__(self,brand,price,color,seating,gear,model):
        super().__init__(brand,price,color,seating)
        self.gear=gear
        self.model=model
        print("Bike class constructor")
b1=Bike('Tata',25000,"black",10,8,9)