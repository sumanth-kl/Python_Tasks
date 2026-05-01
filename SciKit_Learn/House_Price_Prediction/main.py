# Importing required libraries
import numpy as np                  # For numerical operations
import pandas as pd                 # For handling datasets

# Loading dataset
dataset = pd.read_csv("kc_house_data.csv")   # Read CSV file
print(dataset.head())               # Display first 5 rows

# Selecting features (X) and target (y)
X = dataset[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
             'condition', 'grade', 'sqft_basement', 'yr_built', 'yr_renovated']].values
y = dataset['price'].values

# Display shape of data
print('-'*80)
print(f'Shape of X is {X.shape}\nShape of y is {y.shape}')

# Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print('-'*80)
print(f"Length of X_train: {len(X_train)}\nLength of X_test: {len(X_test)}")
print(f"Length of y_train: {len(y_train)}\nLength of y_test: {len(y_test)}")


# -----------------------------
# Feature Scaling
# -----------------------------
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Fit on training data and transform
'''
Different features have different ranges:

Feature	Range    Example
Sepal Length	  1–10
Petal Width	  0.1–2

👉 Problem:

Large values dominate small values
Model becomes biased

👉 Problem:

Large values dominate small values
Model becomes biased

Z=(X−Mean​)/Standard Deviation

👉 After scaling:

Mean = 0
Standard deviation = 1
'''

X_train_scaled = sc.fit_transform(X_train)

'''
This does 2 things:

fit() → learns:
Mean of each column
Standard deviation
transform() → scales data using that info
'''

# Transform test data (important: do NOT fit again)
X_test_scaled = sc.transform(X_test)


from sklearn.metrics import r2_score

# ============================================================
# 1. Multiple Linear Regression
# ============================================================
# Linear Regression models the relationship between features and 
# price by fitting a linear equation (a straight line) to the data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 2. Decision Tree Regression
# ============================================================
# This model breaks down the dataset into smaller subsets while 
# simultaneously developing an associated decision tree (flowchart-like).

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 3. Random Forest Regression
# ============================================================
# An ensemble method that operates by constructing many decision 
# trees and outputting the average prediction of the individual trees.

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 4. Support Vector Regression (SVR)
# ============================================================
# SVR tries to fit the error within a certain threshold (epsilon) 
# instead of just minimizing the error, using kernels for non-linear data.

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 5. K-Nearest Neighbors (KNN)
# ============================================================
# KNN predicts the value of a data point based on how similar it 
# is to its surrounding neighbors in the training set.

from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors=5)
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 6. Gradient Boosting Regression
# ============================================================
# This builds the model in stages; it adds new trees that focus 
# specifically on correcting the errors made by previous trees.

from sklearn.ensemble import GradientBoostingRegressor
regressor = GradientBoostingRegressor(n_estimators=100, random_state=0)
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


# ============================================================
# 7. Ridge Regression
# ============================================================
# A type of linear regression that uses "L2 Regularization" to 
# prevent overfitting by penalizing large coefficients.

from sklearn.linear_model import Ridge
regressor = Ridge(alpha=1.0)
print(regressor)

regressor.fit(X_train_scaled, y_train)
y_pred = regressor.predict(X_test_scaled)

print('\n'+'-'*20+'R2 Score on the Test set'+'-'*20)
print("{:.2f}".format(r2_score(y_test, y_pred)))


"""
# Example: 3 bed, 2 bath, 2000 sqft living, 5000 sqft lot, 2 floors, 
# condition 3, grade 7, 0 basement, built 1990, renovated 0
new_house = [[3, 2, 2000, 5000, 2, 3, 7, 0, 1990, 0]]

# 1. Scale the input using the existing scaler 'sc'
new_house_scaled = sc.transform(new_house)

# 2. Predict using your chosen regressor (e.g., Gradient Boosting)
predicted_price = regressor.predict(new_house_scaled)

print(f"The predicted price of the house is: ${predicted_price[0]:,.2f}")
"""
