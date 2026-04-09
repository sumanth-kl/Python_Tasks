"""2. Device Sensor Value (Scalar Array) An IoT device records a single sensor reading = 75.
Task:
● Create a 0-D NumPy array with this value.
● Print the value and check its number of dimensions."""

import numpy as np

r=(75)
print(type(r))
s=np.array(r)
print(type(s))
print("Value in array is:",s,"\nAnd it's dimesion is:",s.ndim)
