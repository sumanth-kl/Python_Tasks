"""10. Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part"""

import numpy as np

li=[12, 7, 25, 3, 18, 10]
print(li,type(li))
arr=np.array(li)
print(arr,type(arr))

srt_arr=np.sort(arr)
print("Sorted array is",srt_arr)

sp=np.array_split(srt_arr,2)
print("1st split is:",sp[0],"\n2nd split is:",sp[1])
print("Sum os 1st split is:",sp[0].sum())
print("Sum os 2nd split is:",sp[1].sum())
