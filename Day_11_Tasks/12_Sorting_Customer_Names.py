"""12. Sorting Customer Names A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically."""

import numpy as np

cst=["Ravi", "Anil", "Sita", "John"]
print(cst,type(cst))

cst_name=np.array(cst)
print(cst_name,type(cst_name))

srt=np.sort(cst_name)
print("Sorted names:",srt)
