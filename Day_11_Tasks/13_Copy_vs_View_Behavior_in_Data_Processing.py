"""13. Copy vs View Behavior in Data Processing
Scenario: A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference."""

import numpy as np

ds=np.array([10, 20, 30, 40])
print("Original array:",ds)

cp_ds=ds.copy()
print("Copied array:",cp_ds)
ds[1]=int(input("Enter an integer value for ind 1: "))
print("Modified original at ind 1:",ds,"\nUnchanged copy:",cp_ds)

vw_ds=ds.view()
print("View of original:",vw_ds)
vw_ds[3]=int(input("Enter an integer value ind 3: "))
print("Modified view at ind 3:",vw_ds)
print("After modifing view, original is:",ds)
