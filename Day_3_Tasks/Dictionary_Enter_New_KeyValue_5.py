# 5. Write a program to add a new key-value pair to a dictionary.

d={1: 'a', 2: 'b', 3: 'c'}
print(d)
d[4]=['new']
print(d)

nk=input("Enter a key ")
nv=input("Enter the value ")

d[nk]=[nv]
print(d)
