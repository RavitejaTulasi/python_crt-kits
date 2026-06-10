class Player:
    def __init__(self,p_name):
        self.p_name=p_name
class Match:
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
class Tournament:
    def report(self,p,m):
        score=m.s1+m.s2+m.s3
        status="QUALIFIED" if score>=400 else "NOT QUALIFIED"
        print("="*50)
        print("            TOURNAMENT REPORT")
        print("="*50)
        print()
        print("Player Name :",p.p_name)
        print()
        print("Final Score :",score)
        print()
        print("Rank Status :",status)
        print()
        print("="*50)
name=input("Player : ")
print("\nScores :")
s1=int(input())
s2=int(input())
s3=int(input())
p=Player(name)
m=Match(s1,s2,s3)
t=Tournament()
t.report(p,m)