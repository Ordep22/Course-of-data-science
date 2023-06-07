import math
class CirArea():

    def __init__(self,radius = 6):

        self.radius = radius

    def area(self):

        return (self.radius*self.radius)*math.pi

    def setRadius(self, newRadius):
            self.radius = newRadius


    def getRadius(self):
        return self.radius


area = CirArea()
print(f"The radius is: {area.getRadius()}")
print(f"The area is: {area.area()}")
print("\n")

area = CirArea(7)
print(f"The radius is: {area.getRadius()}")
print(f"The area is: {area.area()}")
print("\n")



