# 2. Rectangle Area Calculator (Constructor) A geometry application needs to calculate the area of rectangles. Create a Rectangle class that uses a constructor to initialize length and width. Add a method to calculate and display the area.

class Area:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Rect(self):
        print("Area of Rectangle is",self.length*self.width)

a=Area(3,5)
a.Rect()
