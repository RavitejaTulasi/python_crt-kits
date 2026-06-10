class Passanger:
    def __init__(self):
        self.names=[]
    def register_passanger(self,name):
        self.names.append(name)

class Flight:
    def __init__(self,fno):
        self.fno=fno
class Airport:
    def __init__(self):
        self.seat=[]
        set(self.seat)
    def assign_seat(self,seats):
        if seats in self.seat:
            return "Seat is occupied"
        else:
            self.seat.append(seats)
            return "Check-In Complete"
    def generate_boarding_pass(self,pname,fno):
        print("="*50)
        print("Boarding pass")
        print("="*50)
        print(f"Passanger Name: {pname.names} \n Flight number : {fno.fno} \n Seat number : {self.seat}")
        print(f"Status :{self.assign_seat(self.seat)}")
        print("="*50)
p=Passanger()
p.register_passanger("ravi")
f=Flight("AI202")
a=Airport()
a.assign_seat("12A")
a.generate_boarding_pass(p,f)

