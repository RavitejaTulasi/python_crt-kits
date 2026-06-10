class Customer:
    def __init__(self,c_name):
        self.c_name=c_name
class Movie:
    def __init__(self,movie_name,price):
        self.movie_name=movie_name
        self.price=price
class Booking:
    def __init__(self):
        self.total=0
    def book_ticket(self,num):
        self.num=num
    def calculate(self):
        self.total=m.price*self.num
    def generate_bill(self,c,m):
        print("="*50)
        print("\tMovie Booking Receipt\t")
        print("="*50)
        print(f"Customer Name: {c.c_name}\n Movie Name: {m.movie_name}\n")
        print(f"Ticket price: {m.price}\n Tickets Booked: {self.num}")
        print("-"*50)
        print(f"Total Amount:  {self.total}\n Booking status : CONFIRMED")
        print("="*50)
c=Customer("jhon")
m=Movie("jersy",250)
b=Booking()
b.book_ticket(10)
b.calculate()
b.generate_bill(c,m)