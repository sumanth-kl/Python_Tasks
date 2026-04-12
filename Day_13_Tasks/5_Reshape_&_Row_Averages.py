"""5. Reshape & Row Averages
A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row"""

import numpy as np

data = np.arange(1, 13)
print(data)

d1=data.reshape(3,4)
print("After reshaping matrix is\n",d1)

for index, s in enumerate(d1):
    t=sum(s)
    avg=t/4
    print("Average row{} is {}".format(index+1,avg))
