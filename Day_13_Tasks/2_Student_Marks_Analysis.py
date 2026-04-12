"""2. Student Marks Analysis
Given marks of 5 students in 3 subjects:
marks = np.array([
[70, 80, 90],
[60, 75, 85],
[50, 65, 70],
[90, 95, 85],
[40, 55, 60]
])
Task:
● Calculate total marks of each student.
● Identify students whose total marks are above the class average."""

import numpy as np

marks = np.array([
[70, 80, 90],
[60, 75, 85],
[50, 65, 70],
[90, 95, 85],
[40, 55, 60]
])

tm=[]
for m in marks:
    t=0
    for n in m:
        t=t+int(n)
    tm.append(t)
print("Total marks of individual students are",tm)

dim=np.ndim(marks)+1
print("total subjects are",dim)

avg=[]
av=0
for i in tm:
    if i>0:
        av=i/dim
        avg.append(av)
for index, a in enumerate(avg):
    print("Student {} average is {:.2f}".format(index+1,a))

cavg=sum(avg)
#print(cavg)
l=len(avg)
print("Total number of students is",l)
fcavg=cavg/l
print("Whole class average is",fcavg)

for index, a in enumerate(avg):
    if a > fcavg:
        print("Student {} with average {:.2f}".format(index + 1, a))





