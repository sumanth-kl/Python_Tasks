"""10. University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information."""

class Staff:
    def __init__(self, name):
        self.name=name

class Professor(Staff):
    def display(self):
        print("Professor Name is ",self.name)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant Name is ",self.name)

class Administrator(Staff):
    def display(self):
        print("Administrator Name is ",self.name)

prof=Professor("Virat")
lab=LabAssistant("Rajath")
admin=Administrator("Patidar")

prof.display()
lab.display()
admin.display()
