class Guest:
    def __init__(self,g_name):
        self.g_name=g_name
class Room:
    def __init__(self,r_type,rate):
        self.r_type=r_type
        self.rate=rate
class Reservation:
    def bill(self,nights,rate):
        return nights*rate
    def invoice(self,g,r,nights,amt):
        print("="*50)
        print("              HOTEL INVOICE")
        print("="*50)
        print()
        print("Guest Name     :",g.g_name)
        print("Room Type      :",r.r_type)
        print()
        print("Nights Stayed  :",nights)
        print()
        print("Total Amount   : Rs",amt,sep="")
        print()
        print("="*50)
name=input("Guest Name : ")
r_type=input("Room Type  : ")
nights=int(input("Nights     : "))
rate=int(input("Room Rate  : RS"))
g=Guest(name)
r=Room(r_type,rate)
res=Reservation()
amt=res.bill(nights,rate)
res.invoice(g,r,nights,amt)