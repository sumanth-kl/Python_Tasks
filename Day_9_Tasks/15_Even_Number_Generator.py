"""15. Infinite Even Number Generator (Generators)
Create a generator function that continuously generates even numbers starting from2. The program should print the first N even numbers using this generator."""

def even_num():
    num=2
    while True:
        yield num
        num=num+2

n=even_num()
num=int(input("Enter limit "))
count=0

for i in n:
    print(i)
    count=count+1
    if count==num:
        break
