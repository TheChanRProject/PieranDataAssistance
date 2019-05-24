class Circle():

    #class object attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius

    #method
    def get_circumference(self):
        return (self.radius * self.pi * 2)
