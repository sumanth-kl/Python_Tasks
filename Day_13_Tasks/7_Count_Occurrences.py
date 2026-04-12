"""7. Count Occurrences
You have:
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
Task:
● Count how many times each unique number appears.
● Return numbers with their counts."""

import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])
print("Numbers in the array are\n",data)
num=int(input("Enter a number from the above list "))

count=0
for n in data:
    if n==num:
        count += 1
print("The number ",num,"occurs",count,"time")
        
