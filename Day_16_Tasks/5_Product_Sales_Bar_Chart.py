"""5. Product Sales Bar Chart
Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df=pd.DataFrame({'Product':products,'Sales':sales})

plt.bar(df['Product'],df['Sales'],color='green')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product_Sales_Bar_Chart')
plt.savefig('Product_Sales_Bar_Chart.png')
plt.show()
