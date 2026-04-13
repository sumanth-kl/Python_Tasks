"""7. Replace Values Using NumPy + Pandas A Series:
S = pd.Series([10, 50, 30, 80, 20])
Task:
● Replace values greater than 40 with 0 using NumPy logic
● Return updated Series"""

import pandas as pd  
import numpy as np

S = pd.Series([10, 50, 30, 80, 20])
print(S)

fl = pd.Series(np.where(S > 40, 0, S))
print(fl)
