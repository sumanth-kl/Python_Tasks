"""11. Filter High Temperature Values A weather station records temperatures:
[28, 31, 35, 27, 40, 22]
Scenario: The system needs temperatures above 30°C.
Task:
● Filter the values greater than 30 using NumPy boolean filtering."""

import numpy as np

t=np.array([28, 31, 35, 27, 40, 22])
for n in t:
    if n>30:
        n==True
        print(n)

ht=[False,True,True,False,True,False]
bht=t[ht]
print(bht)
