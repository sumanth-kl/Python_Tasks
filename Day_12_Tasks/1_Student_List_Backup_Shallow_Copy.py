"""1. Student List Backup (Shallow Copy) A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario: She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected."""

marks=[50, 60, 70, 80]
print("1st marks are",marks)
backup=marks
backup[0]=77
#backup[3]=10
print("After modifying",'\n',marks)
print(backup)
print("as i assigned marks to backup variable, any changes in backup will affect marks. and shallow copy is not used because it work with nested objects")
