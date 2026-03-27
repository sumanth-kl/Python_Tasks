# 5. Write a function to check whether a number is even or odd.

num=int(input("Enter a number "))

def pos(num):
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

pos(num)
