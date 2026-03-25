# 7. Write a program to check whether a key exists in a dictionary.

d={1: 'a', 2: 'b', 3: 'c'}
k=int(input("Enter key "))
if k in d:
    print(k,"Exist")
else:
    print(k,"Not Exist")
print(d)
