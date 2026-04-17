"""8. Pie Chart with Conditional Data
Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

scores = np.array([40, 60, 80, 30, 90])

passed_std=scores[(scores>50)]
failed_std=scores[(scores<=50)]

count_pass=np.count_nonzero(passed_std)
count_fail=np.count_nonzero(failed_std)

labels = ['Pass', 'Fail']
counts = [count_pass, count_fail]
explode = (0.01, 0)

plt.pie(counts, labels=labels, explode=explode, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Pass vs Fail Ratio')
plt.savefig('Pass_vs_Fail_Ratio.png')
plt.show()
