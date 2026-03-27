"""5. Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number.
● After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number."""

import random
import math

count=5
while count>=1:
    num=int(input("Enter a number between 1 to 50 : "))
    ran=random.randint(1,50)
    if ran==num:
        print("Your guess is CORRECT!",ran,num)
    else:
        print("Wrong, the number was",ran,"Try again!")
        diff=math.fabs(ran-num)
        print("You are",diff,"numbers away from gussing!")
        count-=1
        print("You left with",count,"choices. Want to Restart again!!!")
