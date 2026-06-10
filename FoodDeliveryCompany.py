class Customer:
    def __init__(self):
        pass
    def delivery_charge(self):
        print("Delivery charges of Rs50")
class PrimeCustomer:
    def __init__(self):
        pass
    def delivery_charge(self):
        print("A discounted Delivery charge of RS20")

c1=Customer()
c1.delivery_charge()
C2=PrimeCustomer()
C2.delivery_charge()