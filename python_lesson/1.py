from math import pi
class SquareIntoCircle:
    def __init__(self, r):
        self.r = round(2 * r / pi, 3)
        self.ploshad = round(4 / pi * r * r, 3)
    def size(self):

        return self.r
    def area(self):

        return self.ploshad
class CircleIntoSquare:
    def __init__(self, storona):
        self.storona = round(pi * storona / 2 , 3)
        self.ploshad = round(pi * pi * storona * storona / 4, 3)
    def size(self):
        return self.storona
    def area(self):

        return self.ploshad
sq = SquareIntoCircle(1)
print(sq.size(), sq.area(), sep='\n')
print()
circle = CircleIntoSquare(sq.size())
print(circle.size(), circle.area(), sep='\n')
