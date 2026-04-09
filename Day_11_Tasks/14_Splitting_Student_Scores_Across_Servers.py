"""14. Splitting Student Scores Across Servers
A dataset:
[50, 60, 70, 80, 90, 100, 110, 120]
Scenario: A distributed system needs to divide this data among 4 servers.
Task:
● Convert to NumPy array.
● Split the array into 4 equal parts using array_split()."""

import numpy as np

m=[50, 60, 70, 80, 90, 100, 110, 120]
print(m,type(m))
marks=np.array(m)
print(marks,type(marks))

std_marks=np.array_split(marks,4)
print("After spliting:",'\n',std_marks)
