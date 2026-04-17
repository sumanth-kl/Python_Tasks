"""6. Multi-Line Graph for Sales Comparison
Scenario:
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]}
Task:
● Create DataFrame
● Plot two line graphs on same plot
● Add legend"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]}

df=pd.DataFrame(data)

plt.plot(df['Month'],df['Store_A'],'g',label='Store A',linewidth=5)
plt.plot(df['Month'],df['Store_B'],'r',label='Store B',linewidth=5)
plt.legend()
plt.title('Sales_Comparision_Multi_Line_Graph')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.savefig('Sales_Comparision_Multi_Line_Graph.png')
plt.show()
