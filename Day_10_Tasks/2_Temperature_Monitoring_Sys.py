"""2. Temperature Monitoring System A weather station records temperatures for two days.
Scenario: Day 1: [30, 32, 31] Day 2: [29, 33, 34]
Task:
● Create a 2D NumPy array to store this data.
● Print the array.
● Find the total temperature recorded."""

import numpy as np

Day1=[30, 32, 31]
Day2=[29, 33, 34]

arr=np.array([Day1,Day2])
print(arr)

t=sum(arr)
print("Day 1 Temp is:",t[0])
print("Day 2 Temp is:",t[1])
print("Day 3 Temp is:",t[2])

print("Total temp recorded is:",t.sum())
