"""7. Convert Float Prices to Integer A shop stores product prices:
[10.5, 20.8, 15.3]
Scenario: The billing system requires integer values.
Task:
● Convert the array from float to integer using astype()."""

import numpy as np

price=np.array([10.5, 20.8, 15.3])
print(price,price.dtype)

pr=price.astype('i')
print(pr,pr.dtype)
