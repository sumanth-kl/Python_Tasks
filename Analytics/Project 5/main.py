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

#===========================================================================================================================
#�� Scenario 6: Car Age Category Analysis + Bar Chart
#===========================================================================================================================
# 6.1 Create a new column 'Car Age Category' using Pandas logic
def get_age_category(year):
    if year >= 2015:
        return "New"
    elif 2010 <= year <= 2014:
        return "Medium"
    else:
        return "Old"

df['Car Age Category'] = df['Year'].apply(get_age_category)

# 6.2 Count the number of cars in each category
age_counts = df['Car Age Category'].value_counts()

# 6.3 Convert category names and counts into NumPy arrays
categories = np.array(age_counts.index)
counts = np.array(age_counts.values)

# 6.4 Plot a bar chart using Matplotlib
plt.bar(categories, counts, color=['#2ecc71', '#f1c40f', '#e74c3c']) # Green, Yellow, Red

# 6.5 Add title and labels
plt.title('Car Distribution by Age Category')
plt.xlabel('Car Age Category')
plt.ylabel('Count')

# 6.6 Save the graph
plt.savefig('Graphs/car_age_category_distribution.png')
plt.show()
