# 10. Write a program to remove duplicate characters from a string.

st1="er2abclkjfdsabcer"
print(st1)
new=''
for char in st1:
    if char not in new:
        new=new+char
print(new)
