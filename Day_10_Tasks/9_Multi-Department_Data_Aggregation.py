"""9. Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total."""

import numpy as np

BranchA=np.array([[10,20],[30,40]])
BranchB=np.array([[5,15],[25,35]])
print(BranchA,'\n',BranchB)

com=BranchA+BranchB
print("Combined Matrice is",'\n',com)

total_emp=com.sum()
print("Total Employees are:",total_emp)
