"""9. Smart Data Processing Pipeline
Scenario: A system processes numeric data from file.
Task:
● Read numbers from a file
● Use NumPy for calculations (mean, std)
● Convert results to Pandas DataFrame
● Use exception handling for bad data
● Use a generator to stream data
● Apply decorator to measure execution time"""

import numpy as np
import pandas as pd
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end-start)
    return wrapper

def read_numbers(filename):
    for line in open(filename, "r"):
        try:
            yield float(line.strip())
        except ValueError:
            continue 

@timer
def process_data():
    nums = list(read_numbers("data.txt"))
    stats = {"Mean": np.mean(nums), "Std_Dev": np.std(nums)}
    df = pd.DataFrame([stats])
    print(df)

process_data()
