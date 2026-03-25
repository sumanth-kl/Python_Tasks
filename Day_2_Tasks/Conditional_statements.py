# 1. Write a program to check whether a number is positive, negative, or zero.
print("Enter a number")
num=int(input())
if num==0:
    print("Number is ZERO")
elif num>0:
    print(num,"is Positive Number")
else:
    print(num,"is Negative Number")

# 2. Write a program to check if a person is eligible to vote (age ≥ 18).
print("Enter your age")
age=int(input())
if age>=18:
   print("You are eligible for Voting!")
else:
   print("You are NOT eligible for Voting!")

# 3. Write a program to find the largest of three numbers using if-elif-else.
print("Enter 3 numbers")
num1=float(input())
num2=float(input())
num3=float(input())
if num1>num2 and num1>num3:
    print(num1,"is Largest Number")
elif num2>num1 and num2>num3:
    print(num2,"is Largest Number")
else:
    print(num3,"is Largest Number")

# 4. Write a program to check whether a number is even or odd.
print("Enter a number")
num=int(input())
if num%2==0:
   print(num,"is EVEN Number")
else:
   print(num,"is ODD Number")

# 5. Write a program to assign grades based on marks (for example: A, B, C, Fail).
print("Enter the marks")
num=int(input())
if num>=85:
    print("Your grade is A")
elif num>=60 and num<85:
    print("Your grade is B")
elif num>=35 and num<60:
    print("Your grade is C")
else:
    print("Your grade is Fail")



