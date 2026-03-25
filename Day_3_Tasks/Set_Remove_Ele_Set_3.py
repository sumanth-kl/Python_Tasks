# 3. Write a program to remove an element from a set.

s1={10, 2, 34, 48, 75, 1, 8, 565, 56, 89, 201}
print(s1)
print("Enter a value from set (REMOVE function)")
value=int(input())
s1.remove(value)
print("After removing",value,"Set is",s1,'\n')

print("Enter a value from set (DISCARD function)")
value=int(input())
s1.discard(value)
print("After removing",value,"Set is",s1,'\n')

print("POP removes random value")
s1.pop()
print("After removing",value,"Set is",s1)
