# 6. Write a program to count the number of vowels in a string.

st=input("Enter a string ")

vowels="aeiouAEIOU"
count=0
for char in st:
    if char in vowels:
        count+=1
print(count)
