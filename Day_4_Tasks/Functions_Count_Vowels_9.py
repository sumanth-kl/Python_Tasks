# 9. Write a function that takes a string as input and returns the number of vowels.

st=input("Enter a string ")

def vow(st):
    vowels="aeiouAEIOU"
    count=0
    for char in st:
        if char in vowels:
            count+=1
    print(count)

vow(st)
