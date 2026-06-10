class Customer:
    def __init__(self,c_name,mobile):
        self.c_name=c_name
        self.mobile=mobile
class RechargePlan:
    def __init__(self,plan,amt):
        self.plan=plan
        self.amt=amt
class Recharge:
    def receipt(self,c,p):
        print("="*50)
        print("             RECHARGE RECEIPT")
        print("="*50)
        print()
        print("Customer Name :",c.c_name)
        print()
        print("Plan Selected :",p.plan)
        print()
        print("Amount Paid   : Rs",p.amt,sep="")
        print()
        print("Status        : SUCCESSFUL")
        print()
        print("="*50)
name=input("Customer : ")
mobile=input("Mobile   : ")
plan=input("Plan     : ")
amt=int(input("Amount   : Rs"))
c=Customer(name,mobile)
p=RechargePlan(plan,amt)
r=Recharge()
r.receipt(c,p)