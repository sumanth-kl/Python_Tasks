"""5. Employee Management System (OOP + File + Dict)
Scenario: Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = {}

while True:
    name = input("Enter Name (or 'done'): ")
    if name == 'done':
        break
    try:
        salary = float(input("Enter Salary: "))
        employees[name] = salary
    except ValueError:
        print("Error: Please enter a numeric value for salary.")
        
try:
    with open("employees.txt", "w") as f:
        for name, salary in employees.items():
            f.write(f"{name}: {salary}\n")
    print("Saved to employees.txt")
except Exception:
    print("File error occurred.")

print("\n--- Employee List ---")
for name in employees:
    print(f"Employee: {name}, Salary: {employees[name]}")
