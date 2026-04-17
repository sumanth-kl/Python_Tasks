"""1. Monthly Sales Line Graph
Scenario: A shop records monthly sales:
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
Task:
● Convert data into a Pandas DataFrame
● Plot a line graph
● Label X-axis as months and Y-axis as sales"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

df = pd.DataFrame({'Month': months, 'Sales': sales})

plt.plot(df['Month'],df['Sales'],marker='o')
plt.title('Line Graph')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('Monthly_sales.jpeg')
plt.show()
