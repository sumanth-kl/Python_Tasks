"""10. Find Indexes of Specific Value A quality check system stores product defect codes:
[2, 4, 1, 4, 3, 4, 5]
Task:
● Find the indexes where value = 4 using NumPy searching."""

import numpy as np

dc=np.array([2, 4, 1, 4, 3, 4, 5])
print(dc)

count=np.where(dc==4)
print("4 found at index values:",count)
