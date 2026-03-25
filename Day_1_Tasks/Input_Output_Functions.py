# 1 Write a Python program that asks the user for their name and prints a greeting message.
print("Enter your name: ")
name=input()
print("Welcome",(name),'\n')

# 2 Take two numbers as input from the user and print their sum.
print("Enter two Numbers: ")
num1=float(input())
num2=float(input())
sum=num1+num2
print("Sum of two numbers is:",sum,'\n')

# 3 Write a program that asks the user for their age and prints the age after 5 years.
print("Please Enter your AGE")
age=int(input())
age=age+5
print("Age after 5 years is:",age,'\n')

# 4 Take a sentence as input and print it in uppercase.
print("Enter your text")
text=input()
uppercase=text.upper()
print(uppercase,'\n')

# 5 Write a program that takes three numbers as input and prints their average.
print("Enter 3 numbers")
num1=float(input())
num2=float(input())
num3=float(input())
average=(num1+num2+num3)/3
print("Average of 3 digits is:", average, '\n')

# 6 Ask the user for a number and print its square.
print("Enter a number")
num=int(input())
#square=num ** 2
square=num*num
print("Squre of number is :",square,'\n')

# 7 Take a user's city name and print: "You live in ___".
print("Enter your city name")
text=input()
print("You Live in ",text,'\n')

# 8 Write a program that takes two numbers and prints their product.
print("Enter a number")
num=int(input())
product=num*num
print("Squre of number is :",product,'\n')

# 9 Ask the user for a temperature in Celsius and print it.
print("Enter the temperature")
temperature=float(input())
print("The temperature is :",temperature,"Celsius",'\n')

# 10 Take two inputs (name and age) and display them in a sentence.
print("Enter name and age")
name=str(input())
age=int(input())
print("Your name is",name,"and you are",age,"years old!")




