"""6. Check Data Type of Inventory Values A warehouse stores product quantities:
[10, 20, 30, 40]
Task:
● Convert it into a NumPy array.
● Print the data type (dtype) of the array."""

import numpy as np

p=[10, 20, 30, 40]
print(p,type(p))
pq=np.array(p)
print(pq,type(pq))
print("Data type is",pq.dtype)
