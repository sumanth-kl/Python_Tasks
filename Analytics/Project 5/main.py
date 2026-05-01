from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

os.makedirs("Graphs", exist_ok=True)

df=pd.read_csv('cardata.csv')

#===========================================================================================================================
#�� Scenario 2: Selling Price Trend (Line Graph)
#===========================================================================================================================
# 2.1 ● Select:  ○ Car_Name  ○ Selling_Price
# 2.2 ● Take the first 10 rows only using Pandas.
first_10=df[['Car_Name','Selling_Price']].head(10)
print(first_10)

# 2.3 ● Convert Selling_Price into a NumPy array.
first_10_arr=first_10['Selling_Price'].to_numpy()

# 2.4 ● Plot a line graph using Matplotlib: ○ X-axis → row index (0–9) ○ Y-axis → Selling Price
plt.plot(first_10_arr, marker='o')

# 2.5 ● Add: ○ title ○ x-axis label ○ y-axis label ○ markers
plt.title('Selling Price Trend of First 10 Cars')
plt.xlabel('Row Index')
plt.ylabel('Selling Price')
plt.tight_layout()
# 2.6 ● Save the graph with a suitable filename.
plt.savefig('Graphs/selling_price_trend.png')
plt.show()
