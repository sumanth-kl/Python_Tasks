# 4. Write a program to check whether an element exists in a tuple.

tup=(10, 2, 34, 48, 75)
print(tup)
print(tup.index(48))
ele=int(input("Enter element: "))
if ele in tup:
    print(tup.index(ele))
else:
    print("element not in tuple")
