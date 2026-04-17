"""4. Temperature Trend Line Plot
Scenario: Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

temps = np.array([28, 30, 32, 31, 29])

pds=pd.Series(temps)

plt.plot(pds,marker='o')
plt.title('Temprature Trend')
plt.grid(True,color='g')
plt.savefig('Temprature_Trend.png')
plt.show()
