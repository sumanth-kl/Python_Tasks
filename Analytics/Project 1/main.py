#=======================================================================
# Project Title: Railway Gauge Data Analysis
# Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
#=======================================================================

# Importing Required Libraries- matplotlib, pandas and numpy
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

"""Scenario 1: Basic Data Loading & Cleaning
Given a CSV file containing railway gauge data.
Tasks:
1. Load the dataset into a Pandas DataFrame.
2. Display the first 5 rows and column names.
3. Check for missing values and replace them with 0.
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types."""

# 1.1 Load the dataset into a Pandas DataFrame.
df=pd.read_csv('railway_gauges_1.csv')

# 1.2 Display the first 5 rows and column names.
print("Top 5 Rows are\n",df.head(),'\n')

# 1.3 Check for missing values and replace them with 0.
# Checking missing values per column
print("Missing values are\n",df.isnull().sum(),'\n')
# Returns only rows with NaN
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)
#Replacing missing values with 0
df.fillna(0, inplace=True)

#1.4 Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
# List of columns to convert
cols = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
# Convert them to numeric, turning errors like '-' or ' ' into NaN
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
#errors='coerce' prevents the code from crashing if there are hidden strings or symbols in CSV.
# Fill any new NaNs with 0 to keep the data clean
df[cols] = df[cols].fillna(0)
print(df.info())
print(df)

#==============================================================================================

"""Scenario 2: Simple Visualization
You want a quick understanding of total railway track growth.
Tasks:
1. Extract Year and Total columns.
2. Plot a line graph showing Total tracks over years.
3. Add:
    ○ Title
    ○ X and Y labels
4. Identify whether the trend is increasing or decreasing."""

#2.1 Extract Year and Total columns.
print(df[['Total','Year']])

#2.2 Plot a line graph showing Total tracks over years.
plt.plot(df['Year'],df['Total'])
plt.xticks(rotation=80)

#2.3 Add: Title X and Y labels
plt.xlabel('Year')
plt.ylabel('Total tracks')
plt.title('Total tracks vs Years')
plt.savefig('Graphs/total_tracks_over_year.png')

#2.4 Identify whether the trend is increasing or decreasing.
plt.show()

#==============================================================================================

"""Scenario 3: Filtering + Bar Chart
You are asked to analyze modern railway expansion.
Tasks:
1. Filter the dataset for years after 2000.
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
3. Plot a grouped bar chart comparing all three gauges.
4. Add legend and proper labels.
5. Identify which gauge dominates in recent years."""

#3.1 Filter the dataset for years after 2000.
#Create a temporary filter without changing df
#This converts '2000-01' -> '2000' -> 2000, just for the comparison
filt = pd.to_numeric(df['Year'].astype(str).str[:4], errors='coerce') > 2000
print(df[filt])

#3.2 Select Broad Gauge, Metre Gauge, and Narrow Gauge.
#3.3 Plot a grouped bar chart comparing all three gauges.
df[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].plot(kind='bar', width=0.8, rot=75)

#3.4 Add legend and proper labels.
plt.title("Comparison of Railway Gauges")
plt.ylabel("Value")
plt.xlabel("Index")
plt.legend()

#3.5 Identify which gauge dominates in recent years.
plt.savefig('Graphs/Broad_Metre_Narrow_bar.png')
plt.show()

#==============================================================================================

"""Scenario 4: Feature Engineering + Pie Chart
You want to analyze the contribution of each gauge type.
Tasks:
1. Calculate total sum of each gauge across all years.
2. Create a new structure (Series/DataFrame) for totals.
3. Plot a pie chart showing percentage contribution.
4. Add percentage labels (autopct).
5. Interpret which gauge contributes the most."""

#4.1 Calculate total sum of each gauge across all years.
broad_sum=sum(df['Broad Gauge'])
metre_sum=sum(df['Metre Gauge'])
narrow_sum=sum(df['Narrow Gauge'])
print(f"Broad Gauge Total is {broad_sum}, Metre Gauge Total is {metre_sum}, Narrow Gauge Total is {narrow_sum}")

#4.2 Create a new structure (Series/DataFrame) for totals.
new_df=pd.Series({'Broad Gauge':broad_sum,'Metre Gauge':metre_sum,'Narrow Gauge':narrow_sum})
print("New Data Series for totals is\n",new_df)

#4.3 Plot a pie chart showing percentage contribution.
#4.4 Add percentage labels (autopct).
plt.clf() # Clear Figure-It is a function used to wipe the current plotting window clean.
plt.pie(new_df.values,labels=new_df.index,autopct='%1.1f%%',explode=(0.01,0.01,0.01),startangle=90)
plt.title('All Gauge contribution')
plt.savefig('Graphs/All_Gauge_contribution.png')

# 4.5 Interpret which gauge contributes the most.
plt.show()

#==============================================================================================

"""Scenario 5: Advanced Analysis + Multiple Graphs
You are asked to perform a complete analysis of railway trends.
 Tasks:
1. Create new columns:
    ○ % Broad Gauge
    ○ % Metre Gauge
    ○ % Narrow Gauge
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
3. Plot:
    ○ Line graph for all gauges
    ○ Stacked bar chart showing composition
4. Highlight:
    ○ Years with highest growth
    ○ Decline in any gauge
5. Provide a final conclusion: 👉 “Is the railway system shifting towards a single dominant gauge?”"""

# 5.1 Create new columns: % Broad Gauge % Metre Gauge % Narrow Gauge
df['% Broad Gauge'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre Gauge'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow Gauge'] = (df['Narrow Gauge'] / df['Total']) * 100
print(df)

# 5.2 Yearly Growth of Total Tracks using np.diff
# We insert a 0 at the start to match the dataframe's row count
growth_values = np.diff(df['Total'])
df['Yearly Growth'] = np.insert(growth_values, 0, 0)
print(df['Yearly Growth'])

# 5.3 Plot: ○ Line graph for all gauges and ○ Stacked bar chart showing composition
for gauge in ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']:
    plt.plot(df['Year'], df[gauge], marker='o', label=gauge)
    
plt.title('Railway Gauge Trends Over Years')
plt.xlabel('Year')
plt.ylabel('Track')
plt.xticks(rotation=80)
plt.legend()
plt.savefig('Graphs/Railway_Gauge_Trends_Over_Years.png')

# Stack the bars using the 'bottom' parameter
# Force the 'Year' column to be strings (helps prevent numeric scaling)
df['Year'] = df['Year'].astype(str)
# Plot the bars
plt.bar(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.bar(df['Year'], df['Metre Gauge'], bottom=df['Broad Gauge'], label='Metre Gauge')
plt.bar(df['Year'], df['Narrow Gauge'], bottom=df['Broad Gauge'] + df['Metre Gauge'], label='Narrow Gauge')

# Manually set the ticks and labels
plt.xticks(ticks=range(len(df['Year'])), labels=df['Year'])

plt.title('Composition of Railway Gauges')
plt.xlabel('Year')
plt.ylabel('Total Track')
plt.xticks(rotation=80)
plt.savefig('Graphs/Composition_of_Railway_Gauges.png')

# 5.4 Highlight: Years with highest growth and Decline in any gauge
highest_growth_val = df['Yearly Growth'].max()
highest_growth_year = df.loc[df['Yearly Growth'].idxmax(), 'Year']

# Decline check
declines = []
for gauge in ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']:
    diffs = np.diff(df[gauge])
    if any(diffs < 0):
        declines.append(gauge)

print(f"Highest Growth: {highest_growth_year} with {highest_growth_val} km")
print(f"Gauges with decline: {', '.join(declines)}")

# 5.5 Final Conclusion
print("\nFinal Conclusion. Yes. The data confirms a rapid shift toward a single dominant gauge (Broad Gauge)")

#============================== End of the File ==============================
