"""1. Sales Threshold Filtering
You are given monthly sales:
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
Task:
● Filter all sales values greater than the average sales
● Return the filtered array."""

import numpy as np

sales=np.array([12000, 18000, 9000, 22000, 15000, 30000])
print("All sales",sales)
l=len(sales)
s=sum(sales)
print("Length of array is",l)
print("Sum of array is",s)
print("Average of sales is",s/l)

sv2=[]
for v in sales:
    if v>s/l:
        sv2.append(True)
    else:
        sv2.append(False)
fl=sales[sv2]
print("Filtered sales value greater than average sales is",fl)
