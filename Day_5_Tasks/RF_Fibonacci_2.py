# 2. Write a recursive function to find the nth Fibonacci number.

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
    
n=int(input("Enter a number "))
print("Fibonacci of",n,"is",fib(n))
