"""4. Product Rating Normalization
Ratings from different users:
ratings = np.array([2, 3, 4, 5, 1])
Task:
● Normalize ratings to a range 0 to 1 using:
normalized = (value - min) / (max - min)"""

import numpy as np

ratings=np.array([2, 3, 4, 5, 1])

mn=np.min(ratings)
mx= np.max(ratings)

normalized=(ratings - mn) / (mx - mn)

print("Original ratings", ratings)
print("Normalized ratings", normalized)
