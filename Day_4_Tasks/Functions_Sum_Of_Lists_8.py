# 8. Write a function to find the sum of elements in a list using a user-defined function.

li=[2,4,5,6,7,21]

def list_total():
    summ=0
    for i in range(li[0],li[-1]):
        summ=summ+li[0]
        #li[0]+=1
        if li[-1]==True:
            break
    print(summ)

list_total()
