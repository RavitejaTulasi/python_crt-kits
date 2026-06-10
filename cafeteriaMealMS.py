class Employee:
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name
class FoodItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Order:
    def __init__(self):
        self.item=[]
    def add_item(self,item):
        self.item.append(item)
    def bill(self,emp):
        print("Employee ID:",emp.emp_id)
        print("Employee Name:",emp.emp_name)
        print("-"*50)
        for i in self.item:
            print(f"{i.name}: \tRs {i.price}")
        print("-"*50)
        print(f"Total Amount:{sum(i.price for i in self.item)}")
        print("Amount status : Paid")
        print("-"*50)
emp1=Employee(101,"John Doe")
order1=Order()
order1.add_item(FoodItem("Burger",150))
order1.add_item(FoodItem("Fries",50))
order1.add_item(FoodItem("Soda",30))
order1.bill(emp1)