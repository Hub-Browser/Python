import math
class circle:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return math.pi*(self.rad**2)
    def peri(self):
        return 2*math.pi*self.rad
rad=float(input("Enter the radius:"))
obj=circle(rad)
print(f"The area is {round(obj.area(),2)} and the perimeter is {round(obj.peri(),2)}")