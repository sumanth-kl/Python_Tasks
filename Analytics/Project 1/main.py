#Basic Data Loading & Cleaning
#Given a CSV file containing railway gauge data.

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#1. Load the dataset into a Pandas DataFrame.
df=pd.read_csv('railway_gauges_1.csv')

#2. Display the first 5 rows and column names.
print("Top 5 Rows are\n",df.head(),'\n')

#3. Check for missing values and replace them with 0.
# Checking missing values per column
print("Missing values are\n",df.isnull().sum(),'\n')

# Returns only rows with at least one NaN
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)

#Replacing missing values with 0
df.fillna(0, inplace=True)
print(df)

#4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0)
print(df.info())
print(df)
#errors='coerce' prevents the code from crashing if there are hidden strings or symbols in CSV.
"""df.iloc[rows, columns]
Breakdown:
: (before the comma): Selects all rows.
1: (after the comma): Selects columns starting from index 1 to the end."""
