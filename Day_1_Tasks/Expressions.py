# 1. Evaluate an expression involving addition and multiplication.
a=10
b=20
c=30
print(a+b*c)
print((a+b)*c,'\n')

# 2. Write an expression to calculate the average of three numbers.
print("Enter 3 numbers")
num1=int(input())
num2=int(input())
num3=int(input())
avg=(num1+num2+num3)/3
print("Average is ",avg,'\n')

# 3. Create a Python expression to calculate the area of a circle.
print("Enter Radius")
r=float(input())
area=3.14159265359*r*r
print("Area of Circle is",area,'\n')

# 4. Write an expression using parentheses to change precedence.
a=10
b=20
c=30
print("Without parantheses",a+b*c)
print("with parantheses",(a+b)*c,'\n')

# 5. Evaluate the expression `10 + 5 * 2`.
exp=10+5*2
print(exp)

# 6. Evaluate `(10 + 5) * 2`.
exp=(10+5)*2
print(exp)

# 7. Write an expression that calculates simple interest.
print("Enter Principle_amount, Interest_rate and Time")
p=float(input())
i=float(input())
t=float(input())
si=(p*i*t)/100
print("Simple Interest is",si,'\n')

# 8. Create a complex expression using multiple operators.
exp1=20+39-19*4/5%2
print(exp1)

# 9. Write an expression to convert Celsius to Fahrenheit.
print("Enter Celsius")
c=float(input())
f=(c*(9/5))+32
print("Fahrenheit is",f,'\n')

# 10. Evaluate an expression with variables.
a=12
b=34
c=56
d=65
e=12
exp=(a+b)-c/d*e
print(exp)

