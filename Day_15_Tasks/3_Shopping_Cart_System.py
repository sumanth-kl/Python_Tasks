"""3. Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except"""


prices={"apple": 10, "orange": 20, "banana": 5}
print("Items in shop and their prices are listed below\n",prices)

total = 0

try:
    item=input("Enter items one after another: ")
    item_list = item.split()
    print(item_list,type(item_list))
    rmv_dplct = set(item_list)

    for i in rmv_dplct:
        if i.isdigit():
            raise ValueError
        if i in prices:
            total += prices[i]
            print(f"Item {i} is {prices[i]} Rs")
        else:
            print(f"Item {i} not in store")
    print(f"Total Bill is {total} Rs")

except Exception:
    print("Please enter item names separated by spaces.")
