# 1. Student Information System (Class & Object) A school wants a program to store student details. Create a Student class with attributes such as name, roll number, and marks. Create objects for at least three students and display their details.
'''
class Student:
    std1_roll_no=1
    std1_name="Virat"
    std1_marks=61
    std2_roll_no=2
    std2_name="Rajath"
    std2_marks=58
    std3_roll_no=3
    std3_name="Jitesh"
    std3_marks=78
    def std(self):
        print(self.std1_roll_no,self.std1_name,self.std1_marks)
        print(self.std2_roll_no,self.std2_name,self.std2_marks)
        print(self.std3_roll_no,self.std3_name,self.std3_marks)
stu=Student()
stu.std()
'''

class Student:
    def __init__(self,std_name,std_roll_no,std_marks):
        self.std_name=std_name
        self.std_roll_no=std_roll_no
        self.std_marks=std_marks

    def std_det(self):
        print("Name",self.std_name)
        print("Roll Number",self.std_roll_no)
        print("Marks",self.std_marks,'\n')

std1 = Student("Jitesh", 1, 55)
std2 = Student("Rajath", 2, 62)
std3 = Student("Virat", 3, 78)

std1.std_det()
std2.std_det()
std3.std_det()
