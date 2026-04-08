"""4. Combine Two Sensor Readings Two sensors record readings during a test.
Scenario: Sensor1 = [10, 20, 30] Sensor2 = [40, 50, 60]
Task:
● Store both readings in NumPy arrays.
● Combine them into one array using NumPy concatenation."""

import numpy as np

Sen1 = [10, 20, 30]
Sen2 = [40, 50, 60]
print(type(Sen1),type(Sen2))

Sensor1=np.array(Sen1)
Sensor2=np.array(Sen2)
print(type(Sensor1),type(Sensor2))

print("Before Concatenation:",Sensor1,Sensor2)
cnct=np.concatenate((Sensor1,Sensor2))
print("After Concatenation:",cnct)
