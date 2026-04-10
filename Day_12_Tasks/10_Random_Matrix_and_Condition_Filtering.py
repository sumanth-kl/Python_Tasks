"""10. Random Matrix and Condition Filtering Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values."""

from numpy import random

mat = random.randint(50, size=(3,3))
print(mat)

for m in mat:
    for n in m:
        if n>25:
            print(n)
