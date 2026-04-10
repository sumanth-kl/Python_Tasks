"""3. Employee Data Copy Issue (Shallow vs Deep Copy) A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy."""

import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]
print("Given list",employees)
emp1=copy.copy(employees)
print("Using Shallow copy",emp1)
emp1[0][1]="Z"
print("After shallow copy, original list",employees)
print("After shallow copy, shallow copied list",emp1)
print("\n Shallow copy feature is whatever changes we do in shallow will be reflected or affect the orginal list\n")
emp2=copy.deepcopy(employees)
print("Before fixing shallow copy",emp2)
emp2[0][1]="A"
print("Using deepcopy to modify",emp2)
print("Unchanged shallow list",employees)
