"""3. Expense Distribution Pie Chart
Scenario: Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
Task:
● Create a pie chart
● Show percentage distribution"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
explode = (0.01, 0.01, 0.01)

fig,ax=plt.subplots()
ax.pie(expenses, explode=explode,labels=labels,autopct='%1.1f%%')
ax.axis('equal')
plt.title('Expence_Pie_Chart')
plt.savefig('Expence_Pie_Chart.jpeg')
plt.show()
