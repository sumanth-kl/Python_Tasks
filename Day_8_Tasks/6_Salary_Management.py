"""6. Employee Salary Management System A company stores employee data in a file employees.txt in the format: EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file."""

'''f=open("Employees.txt","a")
details=input("Enter Name followed by Salary ")
f.write(details + '\n')
f.close()

f=open("Employees.txt","r")
print(f.read())
f.close()

high=[]
f=open("Employees.txt","r")
for h in f:
    part=h.split()
    if len(part)==2:
        high.append(int(part[1]))
high_sal=max(high)
print("Highest salary is",high_sal)
'''

emp={}

f=open("Employees.txt","r")

for line in f:
    part=line.split()
    if len(part)==2:
        name=part[0]
        salary=int(part[1])
        emp[name]=salary

print(emp)

high_sal_name=max(emp, key=emp.get)
high_sal=emp[high_sal_name]

print("Employee with highest salary is",high_sal_name,"and Salry is",high_sal)

