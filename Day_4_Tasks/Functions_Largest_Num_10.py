# 10. Write a Python program with a function that returns the largest of three numbers.

print("Enter 3 numbers")
num1=float(input())
num2=float(input())
num3=float(input())

def lar(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is Largest Number")
    elif num2>num1 and num2>num3:
        print(num2,"is Largest Number")
    else:
        print(num3,"is Largest Number")
        
lar(num1,num2,num3)
