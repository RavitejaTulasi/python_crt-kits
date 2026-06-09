class Employee:
    def __init__(self,empname,empid,job,salary,dept):
        print("Employee Details are: ")
        self.empname=empname
        self.empid=empid
        self.job=job
        self.salary=salary
        self.dept=dept
def Emp_details(self):
    print(f"Employee Name is: {self.empname}")
    print(f"Employee Id is: {self.empid}")
    print(f"Job is: {self.job}")
    print(f"salary is : {self.salary}")
    print(f"Department: {self.dept}")
    print("-"*40)
e1=Employee("Raviteja","23jr","Developer",50000,"AI")
Emp_details(e1)
e2=Employee("teja","23jr2","Developer",50500,"AI")
Emp_details(e2)
e3=Employee("Ravi","23jr1","Developer",55000,"AI")
Emp_details(e3)
e4=Employee("Rteja","23jr3","Developer",54000,"AI")
Emp_details(e4)
e5=Employee("Ravit","23jr4","Developer",53000,"AI")
Emp_details(e5)
e6=Employee("pavam","23jr5","Developer",54000,"AI")
Emp_details(e6)