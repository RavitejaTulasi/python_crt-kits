class Member:
    def __init__(self,m_name):
        self.m_name=m_name
class MembershipPlan:
    def __init__(self,plan,fee):
        self.plan=plan
        self.fee=fee
class Gym:
    def total_fee(self,duration,fee):
        return duration*fee
    def receipt(self,m,p,duration,total):
        print("="*50)
        print("             MEMBERSHIP RECEIPT")
        print("="*50)
        print()
        print("Member Name :",m.m_name)
        print()
        print("Plan        :",p.plan)
        print()
        print("Duration    :",duration,"Months")
        print()
        print("Total Fee   : Rs",total,sep="")
        print()
        print("="*50)
name=input("Member Name : ")
plan=input("Plan        : ")
duration=int(input("Duration    : "))
fee=int(input("Monthly Fee : Rs"))
m=Member(name)
p=MembershipPlan(plan,fee)
g=Gym()
total=g.total_fee(duration,fee)
g.receipt(m,p,duration,total)