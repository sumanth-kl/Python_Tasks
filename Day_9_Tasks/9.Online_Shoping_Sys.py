"""9. Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details."""


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class ElectronicProduct(Product):
    def __init__(self,name,price,warranty):
        Product.__init__(self,name,price)
        self.warranty=warranty
        
class MobilePhone(ElectronicProduct):
    def __init__(self,name,price,warranty,brand):
        ElectronicProduct.__init__(self,name,price,warranty)
        self.brand=brand
    def display(self):
        print("Product is ",self.name)
        print("Amount is ",self.price)
        print("Comes with warranty of ",self.warranty)
        print("Brand is ",self.brand)
        
mob=MobilePhone("Phone",30000,"1 year","IQ00 10R")
mob.display()
