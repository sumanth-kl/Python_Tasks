"""4. Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number"""

import random
import math

ls=[random.randint(1,200) for x in range(20)]
print(type(ls))
print(ls)

print("Maximum num in the list is",max(ls))
print("Minimum num in the list is",min(ls))
print("Square root of maximum number is",math.sqrt(max(ls)))
print("Log of minimum number is",math.log(min(ls)))

print(f"Square root of {max(ls)} is: {math.sqrt(max(ls)):.2f}")
print(f"Log of {min(ls)} is: {math.log(min(ls)):.2f}")

