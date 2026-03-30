# Q2: Develop a Python program for a small shop to process customer purchases. Store product names and prices in a dictionary, items added to the cart in a list, product categories in a set, and product details using tuples. Create functions to display products, add items to the cart, and calculate the total bill. Use a recursive function to compute the total price of all items in the cart. Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError (calculation errors), TypeError (wrong data types in the cart), and NameError (when a product name entered by the user does not exist).

def get_total(prices):
    if not prices:
        return 0
    return prices[0]+get_total(prices[1:])


products={"Pen": 10, "Notebook": 50, "Pencil": 5}
details=(("Pen", "Stationery"), ("Notebook", "Office"))
categories={"Stationery", "Office"}
cart=[]

while True:
    print("\n1. Display Products\n2. Add Item to Cart\n3. View Total Bill\n4. Exit")
    choice=input("Enter choice: ")

    try:
        if choice=='1':
            print("Available Products:")
            for item, price in products.items():
                print(f"{item} : {price}")

        elif choice=='2':
            name=input("Enter product name: ").capitalize()
            if name not in products:
                raise NameError("Product does not exist!")
            
            qty=int(input(f"Enter quantity for {name}: "))
            for n in range(qty):
                cart.append(products[name])

        elif choice=='3':
            if len(cart)==0:
                raise ZeroDivisionError("Cart is empty!")
            
            total=get_total(cart)
            print(f"Total Bill: {total}")

        elif choice=='4':
            break

    except ValueError:
        print("Error: Invalid number entered.")
    except NameError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Wrong data type in cart.")
