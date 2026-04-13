"""6. Remove Outliers
Given data:
values = np.array([10, 12, 15, 18, 100, 14, 13])
Task:
● Compute the mean and standard deviation
● Remove values that are more than 2 standard deviations from the mean"""

import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
std_dev = np.std(values)

low = mean - 2 * std_dev
up = mean + 2 * std_dev

filtered_values = values[(values < low) & (values > up)]

print(mean)
print(std_dev)
print(filtered_values)
