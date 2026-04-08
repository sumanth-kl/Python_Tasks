"""3. Sorting Product Prices An e-commerce company stores product prices in a NumPy array.
Scenario: Prices = [499, 299, 799, 199, 599]
Task:
● Convert it into a NumPy array.
● Sort the prices in ascending order."""

import numpy as np

Prices=[499, 299, 799, 199, 599]
print(type(Prices))

arr=np.array(Prices)
print("After converting to array",arr)
print("Sorted array is",np.sort(arr))
