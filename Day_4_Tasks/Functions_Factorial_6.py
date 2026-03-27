# 6. Write a function that returns the factorial of a number.

num=int(input("Enter a number "))

def fact(num):
    if num<0:
        print("Enter Positive number")
    else:
        factorial=1
        for i in range(1, num+1):
            factorial *= i
        print("The factorial is",factorial)

fact(num)
