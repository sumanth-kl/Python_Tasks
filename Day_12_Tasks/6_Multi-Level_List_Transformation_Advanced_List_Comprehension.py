"""6. Multi-Level List Transformation (Advanced List Comprehension) A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers."""

data = [[1, 2, 3], [4, 5], [6]]
print("Before flattening",data)

flt1=[d for val in data for d in val]
print("After flattening",flt1)

flt2=[v for v in flt1 if v%2==0]
print("Even numbers from flattened list",flt2)
