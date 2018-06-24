class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area is",3.14*self.radius**2)

    def circumference(self):
        print("circumference is", 2*3.14*self.radius)

c1=circle(4)

c1.area()
c1.circumference()
