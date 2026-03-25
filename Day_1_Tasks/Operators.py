# 1. Write a program to add two numbers using arithmetic operators.
num1=10
num2=20
sum=num1+num2
print("Addition of two numbers is",sum,'\n')

# 2. Write a program to check if one number is greater than another.
num1=10
num2=20
print("10>20",num1>num2,'\n')

# 3. Use modulus operator to check if a number is even or odd.
print("Enter a number")
num=int(input())
if num%2==0:
   print(num,"is Even number")
else:
   print(num,"is Odd number")

# 4. Write a program using logical operators to check age eligibility for voting.
print("Enter your age")
age=int(input())
if age>18:
   print("You are eligible for Voting!")
else:
   print("You are NOT eligible for Voting!")

# 5. Demonstrate the use of assignment operators (`+=`, `-=`).
print("NOTE: 5 is the default number used")
print("Enter a number")
num=int(input())
num+=5
print("Using += operator",num)
print("Enter another number")
num=int(input())
num-=5
print("Using -= operator",num)

# 6. Write a program using comparison operators.
print("Enter any two numbers")
num1=input()
num2=input()
if num1==num2:
    print("Numbers are equal")
elif num1>num2:
    print("Number",num1,"is BIGGER")
elif num1<num2:
    print("Number",num2,"is BIGGER")
elif num1!=num2:
    print("Numbers are NOT equal")
else:
    print("TRY again")

# 7. Calculate the power of a number using `**`.
print("Enter a number")
num=int(input())         #ASK for Floating numbers
print("Enter the power")
power=int(input())
print("Power of number is",num**power)

# 8. Use floor division operator to divide two numbers.
print("Enter two numbers")
num1=int(input())
num2=int(input())
div=num1//num2
print("Using floor division operator",div)

# 9. Write a program that checks if two numbers are equal.
print("Enter two numbers")
num1=input()
num2=input()
if num1==num2:
    print("Numbers are equal")
else:
    print("Numbers are NOT equal")

# 10. Combine arithmetic and comparison operators in one expression.
a=10
b=20
c=10
print(a+b>c)


