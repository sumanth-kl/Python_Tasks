# 7. Write a program to convert a tuple to a list and modify the element.
tup1=(10, 2, 34, 48, 75)
print("Creating empty list")
l=[]
print(l)
print("tuple to list conversion")
l=list(tup1)
print(l)
l.append(3456)
print("appending ele 3456",l)

