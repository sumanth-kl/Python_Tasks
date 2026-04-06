"""13. Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function."""


logged_in=False

def secure_login(s_l):
    def wrapper():
        if logged_in==True:
            s_l()
        else:
            print("Error: Access Denied. Login required.")
    return wrapper

@secure_login
def balance():
    print("Your Balance is 10000.00/-")

print("Attempt 1:")
balance()

print("\nAttempt 2:")
logged_in = True
balance()
