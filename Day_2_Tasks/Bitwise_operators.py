# 1. Write a Python program to perform bitwise AND (&) on two numbers entered by the user.
print("Enter two numbers")
num1=int(input())
num2=int(input())
result=num1&num2
print("After AND operation the result is",result,'\n')

# 2. Write a program to perform bitwise OR (|) operation between two integers.
print("Enter two numbers")
num1=int(input())
num2=int(input())
result=num1|num2
print("After OR operation the result is",result,'\n')

# 3. Write a program to demonstrate the bitwise XOR (^) operator using two numbers.
print("Enter two numbers")
num1=int(input())
num2=int(input())
result=num1^num2
print("After XOR operation the result is",result,'\n')

# 4. Write a program to perform left shift (<<) and right shift (>>) operations on a number.
print("Enter two numbers")
num1=int(input())
num2=int(input())
res1=num1<<num2
res2=num1>>num2
print("After LEFT SHIFT operation the result is",res1,'\n')
print("After RIGHT SHIFT operation the result is",res2,'\n')

# 5. Write a Python program that takes a number and prints its bitwise NOT (~) value.
print("Enter a numbers")
num1=int(input())
res=~num1
print("After NOT operation the result is",res,'\n')

