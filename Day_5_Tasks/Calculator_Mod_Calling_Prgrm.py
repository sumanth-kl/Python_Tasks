"""Create a Python module named calculator.py that contains functions to perform:
● Addition
● Subtraction
● Multiplication
● Division
Then write another Python program that imports this module and performs calculations based on user input."""

import calculator as c

print("Default values are 2 and 4")

print("Addition ",c.add(2,4))

print("Subtraction ",c.sub(2,4))

print("Multiplication ",c.mul(2,4))

print("Devison is",c.div(2,4),'\n')

x=int(input("Enter a value "))
y=int(input("Enter another value "))
print("Entered values are",x,y)

print("Addition ",c.add(x,y))

print("Subtraction ",c.sub(x,y))

print("Multiplication ",c.mul(x,y))

print("Devison is",c.div(x,y))
