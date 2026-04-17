"""8. Decorator-based Access Control
Scenario: Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary"""

name = input("Enter Name: ")
role = input("Enter Role: ").lower()
user = {"username": name, "role": role}

def check_admin(func):
    def wrapper():
        if user["role"] == "admin":
            func()
        else:
            print("Access Denied! You are not an admin.")
    return wrapper

@check_admin
def delete():
    print("Database deleted!")

@check_admin
def secrets():
    print("Secret code is 01-11-Mill.")

task = input("What do you want to do? (view secrets/delete DB): ").lower()

if task == "view secrets":
    secrets()
elif task == "delete DB":
    delete()
else:
    print("Unknown task.")

