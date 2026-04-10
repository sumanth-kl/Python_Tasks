"""5. Nested Data Independence (Deep Copy) A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here."""

import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

c1=copy.deepcopy(classes)
print("Deepcopied list",c1)
classes[0][1]=[40,50]
classes[1][1]=[10,43]
print("Modified Original list",classes)
print("Unchanged deepcopy list",c1)
print("\nDeepcopy is required when we only want to modify the original list without affecting the copied list/data")
