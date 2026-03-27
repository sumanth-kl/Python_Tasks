# 4. Write a recursive function to reverse a string.

def rev(s):
    if len(s)<=1:
        return s
    return s[-1]+rev(s[:-1])

s=input("Enter a string ")
print("Reversed string is ",rev(s))
