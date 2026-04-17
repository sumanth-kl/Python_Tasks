"""6. Data Analysis Tool (NumPy + Pandas)
Scenario: Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print results"""

import numpy as np
import pandas as pd

marks = np.random.randint(0, 101, 5)

df = pd.DataFrame(marks, columns=["Marks"])

avg = np.mean(marks)
print("Average Mark:",avg)

for m in df["Marks"]:
    if m >= 40:
        print("Pass:",m)
    else:
        print("Fail:",m)

