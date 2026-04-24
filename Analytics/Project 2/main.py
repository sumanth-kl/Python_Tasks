# ============================================================
# 📊 Project Title: IGN Game Reviews Analysis
# Analyze IGN dataset using NumPy, Pandas, Matplotlib
# ============================================================

# ============================================================
# 📦 1. Import Required Libraries
# ============================================================
# 👉 Import numpy
# 👉 Import pandas
# 👉 Import matplotlib.pyplot
# 👉 (Optional) Import os for folder creation

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

# ============================================================
# 📁 2. Setup Project Structure
# ============================================================
# 👉 Create a folder named "graphs"
# 👉 Ensure it does not throw error if already exists

os.makedirs("Graphs", exist_ok=True)

# ============================================================
# 🟢 SCENARIO 1: Data Loading & Preprocessing
# ============================================================
"""You are given the ign.csv dataset containing game reviews.
👉 Tasks:
1. Load the dataset using Pandas.
2. Display:
    ○ First 5 rows (head())
    ○ Last 5 rows (tail())
    ○ Shape of dataset
3. Remove the unnecessary column:
    ○ "Unnamed: 0" (index column)
4. Check for missing values in:
    ○ score, genre, platform
5. Handle missing values:
    ○ Fill numeric column score with mean
    ○ Fill categorical column genre with mode
6. Ensure correct data types:
    ○ score → float
    ○ release_year, release_month, release_day → integer"""

# 1.1 Load the dataset using Pandas.
df=pd.read_csv('ign.csv')

# 1.2 Display: ○ First 5 rows (head()), ○ Last 5 rows (tail()) and ○ Shape of dataset
print("Top 5 rows from the dataset are\n",df.head())
print("Last 5 rows from the dataset are\n",df.tail())
print("Shape of Dataset is: ",df.shape)

# 1.3 Remove the unnecessary column: ○ "Unnamed: 0" (index column)
df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1, inplace=True) #axis=0 (Rows): The default. axis=1 (Columns)
print(df)

# 1.4 Check for missing values in: ○ score, genre, platform
missing_values=df[['score', 'genre', 'platform']].isna().sum() # for more than 1 column use a list [ ] inside the selection [ ]
print("The total number of missing values are\n",missing_values)

# 1.5 Handle missing values: ○ Fill numeric column score with mean & ○ Fill categorical column genre with mode
score_mean = df['score'].mean()
df['score'] = df['score'].fillna(score_mean)
genre_frequent = df['genre'].mode()[0]
df['genre'] = df['genre'].fillna(genre_frequent)

updated_missing_values=df[['score', 'genre', 'platform']].isna().sum()
print("After updating missing values count are\n",updated_missing_values)

# 1.6 Ensure correct data types: ○ score → float & ○ release_year, release_month, release_day → integer
df['score'] = df['score'].astype(float)
df=df.astype({'release_year':'int','release_month':'int','release_day':'int'})
df.info()

# ============================================================
# 🟢 SCENARIO 2: Line Graph (Score Trend) + Save
# ============================================================
"""You want to analyze how game scores change over time.
👉 Tasks:
1. Group data by release_year.
2. Calculate average score per year using Pandas.
3. Convert results into NumPy arrays.
4. Plot a line graph:
○ X-axis → release_year
○ Y-axis → average score
5. Add:
○ Title: "Average Game Score Over Years"
○ Axis labels
6. Save the graph: plt.savefig("avg_score_trend.png")"""

# 2.1 Group data by release_year.
grp=df.groupby('release_year')

# 2.2 Calculate average score per year using Pandas.
avg=grp['score'].mean()
print(avg)

# 2.3 Convert results into NumPy arrays.
years_arr = avg.index.to_numpy()
scores_arr = avg.to_numpy()
print("Years Array:\n", years_arr)
print("Scores Array:\n", scores_arr)

# 2.4 Plot a line graph: ○ X-axis → release_year & ○ Y-axis → average score
plt.clf()
plt.plot(years_arr,scores_arr,marker='o')

# 2.5 Add: ○ Title: "Average Game Score Over Years" & ○ Axis labels
plt.title('Average Game Score Over Years')
plt.xlabel('Release Year')
plt.ylabel('Average Score')

# 2.6 Save the graph: plt.savefig("avg_score_trend.png")
plt.tight_layout()
plt.savefig('Graphs/avg_score_trend.png')

# ============================================================
# 🟢 SCENARIO 3: Filtering + Bar Chart + Save
# ============================================================
"""You want to compare top platforms.
👉 Tasks:
1. Filter dataset where:
    ○ score > 7
2. Count number of high-rated games per platform.
3. Select top 10 platforms using Pandas.
4. Convert data into NumPy arrays.
5. Plot a bar chart:
    ○ X-axis → platform
    ○ Y-axis → count of games
6. Rotate x-axis labels for readability.
Save the graph: plt.savefig("top_platforms_bar.png")"""

# 3.1 Filter dataset where: ○ score > 7
filt=df[df['score']>7]
print(filt)

# 3.2 Count number of high-rated games per platform.
high_rated = filt['platform'].value_counts()
print(high_rated)

# 3.3 Select top 10 platforms using Pandas.
top_10=high_rated.head(10)
print(top_10)

# 3.4 Convert data into NumPy arrays (to_numpy is the modern method)
    # Convert the platform names (the index) to a NumPy array
platforms_arr = top_10.index.to_numpy()  #platforms_arr = np.array(top_10.index)
    # Convert the counts (the values) to a NumPy array
counts_arr = top_10.to_numpy()  #counts_arr = np.array(top_10)
print("Platforms:", platforms_arr)
print("Counts:", counts_arr)

# 3.5 Plot a bar chart: ○ X-axis → platform & ○ Y-axis → count of games
plt.clf()
plt.bar(platforms_arr,counts_arr)
plt.title('top platforms')

# 3.6 Rotate x-axis labels for readability.
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Graphs/top_platforms_bar.png")

# ============================================================
# 🟢 SCENARIO 4: Aggregation + Pie Chart + Save
# ============================================================
"""You want to analyze genre distribution.
👉 Tasks:
1. Count the number of games per genre.
2. Select top 5 genres using Pandas.
3. Prepare labels and values.
4. Plot a pie chart:
○ Labels → genre
○ Values → count
5. Add percentage labels (autopct).
Save the graph: plt.savefig("genre_distribution.png")"""

# 4.1 Count the number of games per genre.
gen_count=df['genre'].value_counts()
print(gen_count)

# 4.2 Select top 5 genres using Pandas.
top_5=gen_count.head()
print(top_5)

# 4.3 Prepare labels and values.
labels=top_5.index
values=top_5.values

# 4.4 Plot a pie chart: ○ Labels → genre & ○ Values → count
# 4.5 Add percentage labels (autopct).
plt.clf()
plt.pie(values,labels=labels,autopct="%1.1f%%",startangle=90)
plt.title('genre_distribution')
plt.tight_layout()
plt.savefig("Graphs/genre_distribution.png")

# ============================================================
# 🟢 SCENARIO 5: Advanced Analysis + Multiple Graphs
# ============================================================

#You are asked to perform a detailed analysis of review patterns.
# ============================================================
"""👉 Part 5.1: Feature Engineering
1. Create a new column:
    ○ score_category:
        ■ score >= 9 → "Excellent"
        ■ 7 <= score < 9 → "Good"
        ■ < 7 → "Average"
2. Convert editors_choice:
    ○ Y → 1, N → 0"""

df['score_category'] = 'Default'
df.loc[df['score'] >= 9, 'score_category'] = 'Excellent'
df.loc[(df['score'] < 9) & (df['score'] >= 7), 'score_category'] = 'Good'
df.loc[df['score'] < 7, 'score_category'] = 'Average'
print(df['score_category'])

df['editors_choice'] = df['editors_choice'].replace({'Y': 1, 'N': 0})
print(df['editors_choice'])

#=============================================================
"""👉 Part 5.2: NumPy Analysis
3. Use NumPy to:
    ○ Calculate yearly score growth using np.diff() on average yearly scores"""

yearly_averages = df.groupby('release_year')['score'].mean() #Calculate average
diffs = np.diff(yearly_averages) #Calculate growth
yearly_score_growth = np.insert(diffs, 0, 0) #put a '0' in the 1970/1st slot
years = yearly_averages.index
print("Yearly Growth")
for year, growth in zip(years, yearly_score_growth):
    # If the growth is 0, we can label it as the starting year
    if growth == 0:
        print(f"{year}: Starting year (Avg Score: {yearly_averages[year]:.2f})")
    else:
        print(f"{year}: {growth:+.2f}")

#=============================================================
"""👉 Part 5.3: Visualizations
📈 Line Graph
4. Plot trend of:
    ○ Average score per release_year
📊 Stacked Bar Chart
    5. Show count of:
    ○ score_category per release_year
📉 Histogram
    6. Plot distribution of:
    ○ score"""
#Line Graph
plt.clf()
plt.plot(yearly_averages.index,yearly_averages.values,marker='o')
plt.title('Average score per release_year')
plt.xlabel('Release Year')
plt.ylabel('Average score')
plt.tight_layout()
plt.grid(True)
plt.savefig("Graphs/score_trend.png")

#Stacked Bar Chart
count = df.groupby(['release_year', 'score_category']).size().unstack()
print(count)
"""size(): Counts how many games fall into each category for that year.
unstack(): Moves the categories from rows to columns so the plotting tool knows to "stack" them."""
plt.clf()
count.plot(kind='bar', stacked=True)
plt.title('Score Categories per Year')
plt.ylabel('Count')
plt.tight_layout()
plt.legend()
plt.savefig("Graphs/score_category_stacked.png")

#Histogram
plt.clf()
df['score'].hist(bins=30,color='teal', edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.tight_layout()
plt.savefig("Graphs/score_distribution.png")

#=============================================================
"""👉 Part 5.4: Save All Graphs
plt.savefig("score_trend.png")
plt.savefig("score_category_stacked.png")
plt.savefig("score_distribution.png")"""
# saved in Graphs folder

#=============================================================
#👉 Part 5.5: Insights

# ● Which years had highest scores
best_year = yearly_averages.idxmax()
best_score = yearly_averages.max()
print(f"\nYear with high score is {best_year} with the score {best_score}")

# ● Whether high scores increased over time
# Getting the average score of the very first year
first_year_avg = yearly_averages.iloc[0]
first_year = yearly_averages.index[0]

# Getting the average score of the most recent year
last_year_avg = yearly_averages.iloc[-1]
last_year = yearly_averages.index[-1]

# Comparing and printting the insight
print(f"\nIn {first_year}, the average was {first_year_avg:.2f}."
      f"By {last_year}, it changed to {last_year_avg:.2f}.")
if last_year_avg > first_year_avg:
    print("Conclusion: Yes, average scores have increased over time.")
else:
    print("Conclusion: No, average scores have not increased over time.")

# ● If editors_choice correlates with high scores
# Group by editors_choice and calculate the average score
choice_comparison = df.groupby('editors_choice')['score'].mean()

# Print the results
print("\nAverage scores based on Editor's Choice:")
print(f"Not Editor's Choice (0): {choice_comparison[0]:.2f}")
print(f"Editor's Choice (1):     {choice_comparison[1]:.2f}")

# Simple logic check
if choice_comparison[1] > choice_comparison[0]:
    print("Conclusion: Yes, Editor's Choice games correlate with higher scores.")
else:
    print("Conclusion: No, Editor's Choice does not guarantee a higher score.")

#======================End Of the File========================
