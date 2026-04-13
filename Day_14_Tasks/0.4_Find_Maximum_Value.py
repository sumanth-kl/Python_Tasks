"""4. Find Maximum Value A dataset:
arr = np.array([12, 45, 22, 67, 34])
Task:
● Convert to Pandas Series
● Find the maximum value"""

import pandas as pd
import numpy as np

arr = np.array([12, 45, 22, 67, 34])

s=pd.Series(arr)
print(s)
print(s.max())
