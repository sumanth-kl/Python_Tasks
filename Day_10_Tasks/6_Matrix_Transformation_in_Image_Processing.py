"""6. Matrix Transformation in Image Processing An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1, 2],
[3, 4]]
Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices."""

import numpy as np

pix1=np.array([[1,2],[3,4]])
print(type(pix1))
print(pix1)

pix2=np.transpose(pix1)
print("Using transpose:",'\n',pix2)
