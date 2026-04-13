"""5. Filter Values Using Condition A dataset:
arr = np.array([10, 25, 30, 15, 40])
Task:
● Convert to Pandas Series
● Filter values greater than 20"""

import pandas as pd
import numpy as np

arr = np.array([10, 25, 30, 15, 40])

s=pd.Series(arr)
print(s)

print(s[s>20])
