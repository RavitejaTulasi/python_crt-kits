class Vechile:
    def __init__(self,num):
        self.num=num

class Parkingslot:
    def __init__(self,hrs):
        self.hrs=hrs
class parkingmanager:
    def  __init__(self,rate):
        self.rate=rate
    def calculate_parking_fee(self,hrs):
        return self.rate * hrs
    def parking(self):
        print("="*50)
        print("Parking Receipt")
        print("="*50)
        print(f"vechile number : {v.num} \n Hours parked : {p.hrs} \n parking fee : {m.calculate_parking_fee(p.hrs)}")
        print("="*50)
v= Vechile("AP39AB1234")
p=Parkingslot(5)
m=parkingmanager(30)
m.parking()