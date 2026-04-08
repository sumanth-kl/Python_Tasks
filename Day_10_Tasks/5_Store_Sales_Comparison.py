"""5. Store Sales Comparison Two stores record daily sales for 3 days.
Scenario: Store A = [200, 250, 300] Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array."""

import numpy as np

StoreA = [200, 250, 300]
StoreB = [180, 270, 310]

A=np.array(StoreA)
B=np.array(StoreB)
print(A,B)

print("Difference between sales is",A-B)
print("Using abs function to show positive values",abs(A-B))
