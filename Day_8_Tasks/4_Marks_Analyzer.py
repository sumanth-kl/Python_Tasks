"""4. Student Marks File Analyzer A teacher stores student marks in a file marks.txt in the format: Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class"""


'''
f=open("Marks.txt","a")
details=input("Enter Name followed by Marks ")
f.write(details + '\n')
f.close()
'''

f=open("Marks.txt","r")
print(f.read())

num=[]
f=open("Marks.txt","r")
for line in f:
    part=line.split()
    if len(part)==2:
        num.append(int(part[1]))
avg=sum(num)/len(num)
print("Average of class is",avg)
