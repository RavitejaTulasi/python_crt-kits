class Student:
    def __init__(self,stu_id,stu_name,att):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.att=att
        self.student=[]
    def add_student(self,stu):
        self.student.append(stu)

class Assessment:
    def __init__(self,mark):
        self.mark=mark
    def eligibility(self,stu):
        if stu.att >=75 and self.mark >= 60:
            return "ELIGIBLE"
        else:
            return " not ELIGIBLE"
    def generate_report(self,stu):
        print("="*50,"\n","PLACEMENT ELIGIBILITY REPORT","\n","="*50)
        print(f" Student ID : {stu.stu_id} \n Student Name : {stu.stu_name}\n")
        print(f" Attendance : {stu.att} \n Assessment Score : {self.mark}\n Placement Status : {self.eligibility(stu)}\n",'='*50)
stu=Student(123,"ravi",80)
a=Assessment(80)
a.eligibility(stu)
a.generate_report(stu)      
