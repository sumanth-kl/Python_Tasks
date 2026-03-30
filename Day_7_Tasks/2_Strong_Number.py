# 2. Write a program to check whether a given number is a Strong number.

num=int(input("Enter a number: "))
temp=num
total_sum=0

while temp>0:
    digit=temp%10
    fact=1
    for i in range(1, digit + 1):
        fact*=i
        
    total_sum+=fact
    temp//=10

if total_sum==num:
    print("Strong number")
else:
    print("Not a Strong number")
