"""1. Student Marks Analysis A teacher stores the marks of 5 students in a NumPy array.
Scenario: You are given marks [45, 67, 89, 56, 72].
Task:
● Convert the list into a NumPy array.
● Add 5 grace marks to every student.
● Print the updated marks."""

import numpy as np

marks=[45, 67, 89, 56, 72]
print(type(marks))

arr=np.array(marks)
print("List to Array",arr)

print("Adding 5 grace marks",arr + 5)
