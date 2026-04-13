"""1. Convert NumPy Array to Pandas Series A dataset:
arr = np.array([10, 20, 30, 40])
Task:
● Convert this NumPy array into a Pandas Series
● Assign index labels: ["A", "B", "C", "D"]"""

import pandas as pd
import numpy as np

arr = np.array([10, 20, 30, 40])

s=pd.Series(arr,index=["A", "B", "C", "D"])
print(s)

