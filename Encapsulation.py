class BankAccount:
    def __init__(self, name , acc_no,pin):
        self.__name=name
        self.__acc_no=acc_no
        self.__pin=pin
        print("Bank account created successfully")
    def get_name(self):
        print(self.__name)
    def get_acc_no(self):
        print(self.__acc_no)
    def get_pin(self):
        print(self.__pin)
s1=BankAccount('sachin',123456,1234)
s1.get_name()
s1.get_acc_no()
s1.get_pin()