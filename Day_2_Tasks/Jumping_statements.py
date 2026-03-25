# 1. Write a program using break to stop printing numbers when the number reaches 5.
for i in(1,2,3,4,5,6,7,8):
    print(i)
    if (i==5):
        break
print('\n')

# 2. Write a program using continue to skip printing the number 3 in a loop from 1 to 10.
i=0
while (i<10):
    i=i+1
    if i==3:
        continue
    print(i,'\n')

# 3. Write a program that uses pass inside a loop.


# 4. Write a program that searches for a number in a list and breaks the loop when found.
print("Enter the number between 1 to 10")
num=int(input())
list=[1,2,3,4,5,6,7,8,9,10]
found=False
for i in list:
    if i==num:
        print("number found",'\n')
        found=True
        break
if not found:
    print("number not in list",'\n')

# 5. Write a program that prints numbers from 1 to 10 but skips even numbers using continue.
print("Printing even numbers from 1 to 10")
for i in range(1,10,2):
    print(i)



