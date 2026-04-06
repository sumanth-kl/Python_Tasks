#5. Vehicle Management System (Inheritance) A transport company manages different vehicles. Create a base class Vehicle with attributes like brand and speed. Create derived classes Car and Bike that inherit from Vehicle and display their details.

class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
        
class Car(Vehicle):
    def car_det(self):
        print("Car Brand is",self.brand)
        print("Max Speed is",self.speed)

class Bike(Vehicle):
    def bike_det(self):
        print("Bike Brand is",self.brand)
        print("Max Speed is",self.speed)

c1=Car("BMW",300)
c2=Car("AUDI",280)
c1.car_det()
c2.car_det()

b1=Bike("RE",180)
b2=Bike("NS200",200)
b1.bike_det()
b2.bike_det()
