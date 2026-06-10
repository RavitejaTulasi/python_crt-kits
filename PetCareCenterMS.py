class Owner:
    def __init__(self,o_name):
        self.o_name=o_name
class Pet:
    def __init__(self,p_name):
        self.p_name=p_name
class Appointment:
    def __init__(self):
        self.appointments=[]
    def add(self,owner,pet,service,charge):
        self.appointments.append((owner,pet,service,charge))
    def receipt(self,owner,pet,service,charge):
        print("="*50)
        print("            SERVICE RECEIPT")
        print("="*50)
        print()
        print("Owner Name :",owner.o_name)
        print("Pet Name   :",pet.p_name)
        print()
        print("Service    :",service)
        print()
        print("Amount     : Rs",charge,sep="")
        print()
        print("="*50)
o_name=input("Owner Name : ")
p_name=input("Pet Name   : ")
service=input("Service    : ")
charge=int(input("Charge     : Rs"))
o=Owner(o_name)
p=Pet(p_name)
a=Appointment()
a.add(o,p,service,charge)
a.receipt(o,p,service,charge)