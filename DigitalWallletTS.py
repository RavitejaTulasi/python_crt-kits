class User:
    def __init__(self,u_name):
        self.u_name=u_name
class Wallet:
    def __init__(self,bal):
        self.bal=bal
class Transaction:
    def __init__(self):
        self.transactions=[]
    def transfer(self,w,amt):
        w.bal-=amt
        self.transactions.append(amt)
    def receipt(self,u,open_bal,amt,current_bal):
        print("="*50)
        print("          TRANSACTION RECEIPT")
        print("="*50)
        print()
        print("User Name       :",u.u_name)
        print()
        print("Opening Balance : Rs",open_bal,sep="")
        print()
        print("Transfer Amount : Rs",amt,sep="")
        print()
        print("Current Balance : Rs",current_bal,sep="")
        print()
        print("Status          : SUCCESSFUL")
        print()
        print("="*50)
name=input("User          : ")
bal=int(input("Wallet Balance:Rs"))
amt=int(input("Transfer      : Rs"))
u=User(name)
w=Wallet(bal)
t=Transaction()
open_bal=w.bal
t.transfer(w,amt)
t.receipt(u,open_bal,amt,w.bal)