class Client:
    def __init__(self,c_name):
        self.c_name=c_name
class Project:
    def __init__(self,p_name):
        self.p_name=p_name
class Invoice:
    def amount(self,hours,rate):
        return hours*rate
    def receipt(self,c,p,hours,amt):
        print("="*50)
        print("                CLIENT INVOICE")
        print("="*50)
        print()
        print("Client Name   :",c.c_name)
        print("Project Name  :")
        print()
        print(p.p_name)
        print()
        print("Hours Worked  :",hours)
        print()
        print("Total Amount  : Rs",amt,sep="")
        print()
        print("="*50)
name=input("Client       : ")
project=input("Project      : ")
hours=int(input("Hours Worked : "))
rate=int(input("Hourly Rate  : Rs"))
c=Client(name)
p=Project(project)
i=Invoice()
amt=i.amount(hours,rate)
i.receipt(c,p,hours,amt)