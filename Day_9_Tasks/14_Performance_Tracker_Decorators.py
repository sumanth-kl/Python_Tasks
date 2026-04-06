"""14. Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function."""

import time

def cal_time(c_t):
    def wrapper():
        start=time.time()
        c_t()
        end=time.time()
        print("Total Time taken is ",end - start)
    return wrapper

@cal_time
def total_time():
    for i in range(100):
        pass

total_time()
