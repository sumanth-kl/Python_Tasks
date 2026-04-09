"""15. Reshape and Flatten Image Data
Scenario: An image is stored as a 2 × 3 matrix:
[[1,2,3],
[4,5,6]]
Task:
1. Convert it into a NumPy array.
2. Flatten the array into 1-D format.
3. Print the flattened array."""

import numpy as np

i=[[1,2,3],[4,5,6]]
print(i,type(i))
img=np.array(i)
print(img,type(img))

img_rs=img.reshape(-1)
print("After flattening:",img_rs)
