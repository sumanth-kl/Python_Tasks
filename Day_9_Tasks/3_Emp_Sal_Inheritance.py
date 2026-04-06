# 3. Employee Salary System (Simple Inheritance) A company has two types of employees: Employee and Manager. Create a base class Employee containing name and salary. Create a derived class Manager that inherits from Employee and displays the employee details.

"""
class Employee:
    def __init__(self,emp_name,emp_sal):
        self.emp_name=emp_name
        self.emp_sal=emp_sal
        
class Manager(Employee):
    def emp(self):
        print("Employee name is ",self.emp_name)
        print("Employee salary is ",self.emp_sal,'\n')

e1=Manager("Virat",10000)
e2=Manager("Rajath",80000)
e3=Manager("Jitesh",75000)
e1.emp()
e2.emp()
e3.emp()


"""
class Employee:
    emp1="Virat"
    emp1_sal=100000
        
class Manager(Employee):
    def emp(self):
        print("Employee name is", self.emp1)
        print("Employee salary is", self.emp1_sal)

e=Manager()
e.emp()

