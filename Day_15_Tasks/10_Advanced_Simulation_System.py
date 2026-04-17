"""10. Advanced Simulation System
Scenario: Simulate exam results and generate reports.
Task:
● Generate random marks using random
● Store in NumPy array
● Convert to Pandas DataFrame
● Use OOP to represent Student
● Use conditions + loops to assign grades
● Save report to file
● Handle errors using try-except
● Use math module for statistics"""

import random
import numpy as np
import pandas as pd
import math

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = np.array([random.randint(1, 100) for m in range(3)])
        self.avg = self.marks.mean()
        self.grade = "Pass" if self.avg >= 40 else "Fail"

try:
    names = ["Virat", "Jitesh", "Rajath", "David", "Bhuvi"]
    student_list = [Student(n) for n in names]

    data = [[s.name, s.avg, s.grade] for s in student_list]
    df = pd.DataFrame(data, columns=["Name", "Average", "Result"])

    class_avg = df["Average"].mean()

    with open("simple_report.txt", "w") as f:
        f.write(df.to_string(index=False))
        f.write(f"\n\nClass Average: {class_avg}")

    print("Report saved to simple_report.txt")
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")
