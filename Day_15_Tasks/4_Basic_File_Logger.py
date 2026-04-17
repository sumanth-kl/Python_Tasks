"""4. Basic File Logger
Scenario: A system logs user actions.
Task:
● Take user input
● Store logs in a file
● Use loop to allow multiple entries
● Handle file errors using exception handling"""

import time

try:
    with open("logs.txt", "a") as file:
        print("Logging System [Type 'quit' to exit]")
        
        while True:
            action = input("Action: ")
            if action == 'quit':
                break
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {action}\n")
            print("Action Logged")

except BaseException:
    print("System Error, Try again")
