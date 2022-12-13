import math
class Vector:
    def __init__(self,x: float,y: float):
        self.x = x
        self.y = y


    def set(self, x, y):
        self.x = x
        self.y = y
    def set(self, input):
        self.x = input[0]
        self.y = input[1]
    def get(self):
        return[self.x,self.y]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def x(self):
        return self.x
    def y(self):
        return self.y


    def __mul__(self,other):
        if type(other) == type(self):
            return (self.x * other.x)+(self.y * other.y)#dot product
        else:
            return (self.x * other)+(self.y * other)#simple multiplication
    __rmul__ = __mul__


    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x,self.y - other.y)
    def __rsub__(self, other):
        return Vector(other.x - self.x,other.y - self.y)


    def mag(self):
        return math.sqrt(self.x**2 + self.y**2 )
    def angle(self, other):
        return math.acos((self * other)/(self.mag * other.mag))
    def unit(self):
        mag = mag(self)
        return Vector(self.x/mag,self.y/mag)
    def projectedOnto(self,other):
        return other * ((1/other.mag()^2) * (other * self))