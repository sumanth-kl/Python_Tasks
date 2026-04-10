"""7. Filter Positive Even Numbers from Dataset Scenario: A dataset contains mixed values:
arr = [-5, 10, 15, -2, 20, 25, 30]
Task:
● Convert to NumPy array.
● Filter values that are:
○ Positive
○ Even"""

import numpy as np

arr = [-5, 10, 15, -2, 20, 25, 30]
print(arr,type(arr))
val=np.array(arr)
print(val,type(val))

pos=[v for v in arr if v>0]
print("Positive numbers are",pos)

even1=[e for e in arr if e%2==0]
even2=[e for e in pos if e%2==0]
print("Even numbers from original no list",even1)
print("Even numbers from positive no list",even2)
