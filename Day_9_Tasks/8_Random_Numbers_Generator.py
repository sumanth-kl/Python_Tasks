# 8. Random Number Generator (Generators) A program is needed to generate numbers for testing purposes. Create a generator function that produces numbers from 1 to N and prints them one by one when iterated.

import random

def ran_num(n, start=1, end=100):
    for _ in range(n):
        yield random.randint(start, end)

lim = 5
gen = ran_num(lim)

for num in gen:
    print(num)
