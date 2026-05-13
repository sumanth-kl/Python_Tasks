import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score

# 1. Loading & Cleaning
dataset = pd.read_csv("weather_history.csv")
dataset.columns = dataset.columns.str.strip()

# 2. FEATURE ENGINEERING (Fixed Date Logic)
# Find the date column and use it as a string
date_cols = [col for col in dataset.columns if 'Date' in col]
if not date_cols:
    print("Error: Could not find a Date column. Check your CSV headers.")
else:
    actual_date_col = date_cols[0] # Take the first match
    # Fixed: Passing the specific column name, not the whole list
    dataset[actual_date_col] = pd.to_datetime(dataset[actual_date_col], utc=True)
    dataset = dataset.sort_values(by=actual_date_col)

    dataset['Month'] = dataset[actual_date_col].dt.month
    dataset['Hour'] = dataset[actual_date_col].dt.hour
    dataset['Prev_Temp'] = dataset['Temperature_(C)'].shift(1)
    dataset['Temp_Diff'] = dataset['Temperature_(C)'] - dataset['Prev_Temp']
    dataset = dataset.dropna()

# 3. GROUPING FOR 80%+ ACCURACY
# Merging the two categories that confuse the model
dataset['Summary'] = dataset['Summary'].replace(['Partly Cloudy', 'Mostly Cloudy'], 'Cloudy')

# 4. Filter and Encode
top_3 = dataset['Summary'].value_counts().nlargest(3).index
dataset = dataset[dataset['Summary'].isin(top_3)]

le = LabelEncoder()
dataset['Precip_Type'] = le.fit_transform(dataset['Precip_Type'].astype(str))
dataset['Summary'] = le.fit_transform(dataset['Summary'])

# 5. Feature Selection
feature_cols = ['Precip_Type', 'Temperature_(C)', 'Humidity', 'Month', 'Hour', 
                'Prev_Temp', 'Temp_Diff', 'Pressure_(millibars)']

X = dataset[feature_cols].values
y = dataset['Summary'].values

# 6. Split & Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler()
X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

# 7. Training Models
print("Training Models... comparing performance.")
rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=0).fit(X_train_scaled, y_train)
xgb = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=0).fit(X_train_scaled, y_train)
cat = CatBoostClassifier(iterations=300, learning_rate=0.1, depth=6, verbose=0).fit(X_train_scaled, y_train)

# 8. Final Results Output
print('\n' + '='*25 + ' ACCURACY COMPARISON ' + '='*25)
print(f"Random Forest Accuracy: {accuracy_score(y_test, rf.predict(X_test_scaled)):.4f}")
print(f"XGBoost Accuracy:       {accuracy_score(y_test, xgb.predict(X_test_scaled)):.4f}")
print(f"CatBoost Accuracy:      {accuracy_score(y_test, cat.predict(X_test_scaled)):.4f}")
print('='*71)
print(f"Final Groups Predicted: {list(le.classes_)}")


import matplotlib.pyplot as plt

# 1. Get importance scores from the Random Forest model
importances = rf.feature_importances_
indices = np.argsort(importances)

# 2. Plotting
plt.figure(figsize=(10, 6))
plt.title("Feature Importance - What drives the Weather?")
plt.barh(range(len(indices)), importances[indices], color='skyblue', align='center')
plt.yticks(range(len(indices)), [feature_cols[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
