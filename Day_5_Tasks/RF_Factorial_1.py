# 1. Write a recursive function to calculate the factorial of a number.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number "))
f=fact(n)
print("Factorial of",n,"is",f)
