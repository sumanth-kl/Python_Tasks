# 6. Shape Area Calculator (Polymorphism) A graphics application needs to calculate the area of different shapes. Create classes Circle, Rectangle, and Triangle, each having an area() method. Demonstrate polymorphism by calling the same method for different objects.

import math
class Circle:
    def area(self,r):
        print("Area of Circle is",end=" ")
        return r*r

class Rectangle:
    def area(self,l,w):
        print("Area of Rectangle is",end=" ")
        return l*w

class Triangle:
    def area(self,s1,s2,s3):
        sp=(s1+s2+s3)/2
        area=math.sqrt(sp*(sp-s1)*(sp-s2)*(sp-s3))
        print("Area of Triangle is",end=" ")
        return area

c=Circle()
r=Rectangle()
t=Triangle()

c1=int(input("Enter Radius "))
print(c.area(c1))

r1=int(input("Enter Lenght "))
r2=int(input("Enter Width "))
print(r.area(r1,r2))

t1=int(input("Enter side 1 "))
t2=int(input("Enter side 2 "))
t3=int(input("Enter side 3 "))
print(t.area(t1,t2,t3))
