"""12. Random Dataset Normalization + Filtering Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values"""

import numpy as np
from numpy import random
x=random.rand(5)
print(x)

s=[]
for i in x:
    i=i*100
    if i>50:
        s.append(True)
    else:
        s.append(False)
fl=x[s]
print(np.sort(fl))    
