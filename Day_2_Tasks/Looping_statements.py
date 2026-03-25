# 1. Write a Python program to print numbers from 1 to 10 using a for loop.
print("Numbers from 1 to 10")
for i in range (1,11):
    print(i)

# 2. Write a program to print the multiplication table of a number using a loop.
print("Multiplication Table for given Number")
num=int(input())
for i in range (num,(num*10)+1,(num)):
    print(i)

# 3. Write a program to find the sum of numbers from 1 to N using a loop.
print("Sum of numbers")
num=int(input("Enter a number: "))
res=0
for i in range(1,num+1):
    res=res+i   #res+=i
print("Sum from 1 to",num,"is",res)

# 4. Write a program to print all even numbers between 1 and 50.
print("Even Numbers from 1 to 50")
for i in range (2,51,2):
    print(i)

# 5. Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter a number"))
if num<0:
    print("Enter Positive number")
else:
    factorial=1
    for i in range(1, num+1):
        factorial *= i
    print("The factorial is",factorial)


