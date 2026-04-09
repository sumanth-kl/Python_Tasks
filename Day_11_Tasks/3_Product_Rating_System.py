"""3. Product Rating System An e-commerce website stores product ratings:
[4, 5, 3, 4, 2]
Task:
● Convert it to a NumPy array.
● Print the first and last rating using indexing."""

import numpy as np

rat=[4, 5, 3, 4, 2]
print(rat,type(rat))

rat_arr=np.array(rat)
print(rat_arr,type(rat_arr))

print("First element is",rat_arr[0],"Last element is",rat_arr[-1])
