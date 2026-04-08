"""7. Splitting Data for Parallel Processing A dataset contains the following values:
[5, 10, 15, 20, 25, 30]
Scenario: You want to distribute the data across 3 processors.
Task:
● Store the data in a NumPy array.
● Split it into 3 equal parts using NumPy."""

import numpy as np

d=[5, 10, 15, 20, 25, 30]
print(type(d))
data=np.array(d)
print(type(data),'\n',data)

split_data=np.array_split(data,3)
print("After spliting",'\n',split_data)
