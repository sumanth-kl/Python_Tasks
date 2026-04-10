"""11. Boolean Masking for Salary Analysis Scenario: Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition."""

import numpy as np

salary=[25000, 40000, 15000, 50000, 30000]
sal=np.array(salary)
print(sal)

es=[]
for s in sal:
    if s>30000:
        es.append(True)
    else:
        es.append(False)

hs=sal[es]
print(hs)
print(len(hs))
