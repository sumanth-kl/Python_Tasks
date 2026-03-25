# 1. Convert an integer to a float.
print("Enter an Integer")
num=int(input())
print("Before converting",num,type(num))
floating_num=float(num)
print("After converting to float",floating_num,type(floating_num),'\n')

# 2. Convert a float to an integer.
print("Enter an Floating number")
num=float(input())
print("Before converting",num,type(num))
int_num=int(num)
print("After converting to integer",int_num,type(int_num),'\n')

# 3. Convert a string `"123"` to an integer.
string=str(123)
print("Before converting",string,type(string))
int_num=int(string)
print("After converting to integer",int_num,type(int_num),'\n')

# 4. Convert an integer to a string and print it with text.
print("Enter an Integer")
num=int(input())
print("Before converting",num,type(num))
string=str(num)
print("After converting to string",string,type(string),'\n')

# 5. Take a number as input and convert it to an integer.
print("Enter an number")
num=input()
print("Before converting",num,type(num))
integer_num=int(float(num))   #ASK
print("After converting to integer",integer_num,type(integer_num),'\n')

# 6. Convert a float to a string and print it.
print("Enter an Floating number")
num=float(input())
print("Before converting",num,type(num))
string=str(num)
print("After converting to string",string,type(string),'\n')

# 7. Add two numbers taken as strings by converting them to integers.
print("Enter an String")
num1=str(input())
num2=str(input())
print("Before converting",num1,type(num1),num2,type(num2))
nu1=int(num1)
nu2=int(num2)
sum=nu1+nu2
print("After converting to integer",sum,type(sum),'\n')

# 8. Convert `"45.6"` to float.
num1="45.6"
num2=float(num1) #num=float(45.6)
print(num2,type(num2),'\n')

# 9. Convert a number to string and concatenate it with another string.
num1=int(123)
print(num1,type(num1))
string=str(456)
print(string,type(string))
nmbr_string=str(num1)
print("converted number",nmbr_string,type(nmbr_string))
final=string+nmbr_string
print("Added number",final,type(final),'\n')

# 10. Write a program to display the type of converted variable.
num1=int(45)
a=float(num1)
print(type(a))
num2=float(45.67)
b=str(num2)
print(type(b))
num3=str(2345)
c=int(num3)
print(type(c))


