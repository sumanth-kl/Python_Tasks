# 9. Write a program to count the frequency of each character in a string.

st="abcacbgad"
print(st)
fr={}  #Using Dictionary
for char in st:
    fr[char]=fr.get(char,0)+1
print(fr)
