import math
class Circle():

    #class object attribute


    def __init__(self, radius):

        self.radius = radius
        self.pi = math.pi
    #method
    def get_circumference(self):
        return round((self.radius * self.pi * 2), 2)


circ = Circle(radius=10)

print(circ.get_circumference())
