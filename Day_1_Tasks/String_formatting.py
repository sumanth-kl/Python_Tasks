# 1. Print a name and age using string formatting.
name='Sumanth'
age='1'
txt=f"My name is {name} and age is {age}"
print(txt)

# 2. Format a string using `format()` method.
txt='My name is {fname}, I am {age}'.format(fname='Sumanth',age=1)
print(txt)

# 3. Use **f-strings** to print a sentence with variables.
name='Sumanth'
birth_date=1
print(f"My name is {name} and my Birth date is {birth_date}")

# 4. Display a floating number with 2 decimal places.
c=29.98
print(c)

num=25.786425
print(f"The number is {num:.2f}")

# 5. Print a formatted price value.
price=158.76
print("The price is {:.0f}".format(price))

txt='For any {price:.2f} INR'
print(txt.format(price=777))

# 6. Create a sentence using two variables with formatting.
name='Sumanth'
place='shimogga'
txt=f"{name} from {place}"
print(txt)

# 7. Format a number with commas (100000 → 100,000).
num=100000
print("{:,}".format(num))

# 8. Display a percentage using string formatting.
num=87.5
print("{:.2%}".format(num))

# 9. Align text using formatting.
name = "Sumanth"

print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")


# 10. Print a table row using formatted strings.
data=[("Apples",50),("Bananas",120),("Grapes",8)]
print(f"{'Item':<10} | {'Price':>8}")
print("-" * 21)
for item, price in data:
    print(f"{item:<10} | {price:>8.2f}")
