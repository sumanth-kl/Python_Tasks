# 8. Write a program to check whether a string is a palindrome.

st=input("Enter a string ")
rev=st[::-1]
if st==rev:
    print("string is palindrome")
else:
    print("String is NOT palindrome")
