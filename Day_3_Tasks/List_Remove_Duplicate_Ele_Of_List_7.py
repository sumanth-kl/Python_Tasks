# 7. Write a program to remove duplicate elements from a list.
l=[2,4,6,3,7,6]
l=list(set(l))
print(l)


# Second method

list1=[6,2,4,6,3,7,6]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("before",list1)
print("after",list2)
