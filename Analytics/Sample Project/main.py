from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#loading csv file
df=pd.read_csv('railway_gauges.csv')

#printing top 5 rows along with column names
print("Top 5 Rows are\n",df.head(),'\n')

#finding which year has maximum installations
print(df.iloc[[df['Total'].idxmax()]])

#plot data using bar chart
ax=df.plot(x='Year',kind='bar')
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Gauges: Number of railway tracks installed per year')
plt.savefig('Graphs/rail_gauges.png')
plt.show()
