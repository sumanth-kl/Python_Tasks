"""8. Random Sales Simulation Scenario: A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales."""

from numpy import random

sales=random.randint(100,500, size=(10))
print(sales)

print("Total sales is",sum(sales))

avg=sum(sales)/10
print("Average of sales for 10 days is",avg)
