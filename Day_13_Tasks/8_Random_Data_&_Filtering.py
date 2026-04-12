"""8. Random Data & Filtering
Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result."""

import numpy as np

nums = np.random.randint(1, 100, 10)
print("Generating random numbers from 1 to 100\n",nums)

l=[]
for n in nums:
    if n%5==0:
        l.append(True)
    else:
        l.append(False)
fl=nums[l]
print("SOrted numbers which are devisible by 5\n",np.sort(fl))
