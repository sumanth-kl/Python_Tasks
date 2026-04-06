"""17. Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it."""

def bonus_decorator(b_d):
    def wrapper(self):
        self.salary=self.salary+500
        b_d(self)
    return wrapper

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @bonus_decorator
    def show(self):
        print("Employee:",self.name)
        print("Salary with Bonus:",self.salary)

emp=Employee("Virat",10000)
emp.show()
