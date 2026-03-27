# 3. Write a recursive function to calculate the sum of digits of a number.

def digits(n):
    if n < 10:
        return n
    return (n % 10) + digits(n // 10)
n=int(input("Enter a number "))
print("Sum is ",digits(n))
