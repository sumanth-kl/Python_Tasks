"""2. Random Number Analyzer
Scenario: A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates"""

import random

l=[random.randint(1,100) for i in range(10)]
print(l,type(l))

e=0
o=0
for n in l:
    if n%2==0:
        e+=1
    else:
        o+=1
print(f"Even numbers count is: {e} \nOdd numbers count is: {o}")

s=set(l)
print(l,type(s))
