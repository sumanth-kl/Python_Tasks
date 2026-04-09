"""5. Accessing Matrix Data A teacher stores marks of students in two subjects:
[[78, 85],
[90, 88],
[67, 72]]
Task:
● Convert it to a NumPy array.
● Access the second student's second subject mark."""

import numpy as np

m=[[78, 85],[90, 88],[67, 72]]
marks=np.array(m)
print(type(marks),'\n',marks)

print("Second student marks are:",marks[1:2])
