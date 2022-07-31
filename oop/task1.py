from math import sqrt

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @property
    def mag(self):
        return sqrt(self.x**2 + self.y**2)

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def movX(self, newx):
        self.x = newx

    def movY(self, newy):
        self.y = newy

    def showPoint(self):
        return f'The points are ({self.x}, {self.y})'

## Main Program
p1 = Point()
p2 = Point(3, -4)

p2.move(5,5)

print(p2.mag)
print(p2.showPoint())
