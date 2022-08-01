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
from random import randint

def addPoints(p1, p2):
    return Point(p1.x + p2.x, p1.y + p2.y)

l1 = [Point(randint(-10,10), randint(-10,10)) for i in range(5)]
l2 = [Point(randint(-5,5), randint(-5,5)) for i in range(5)]
l3 = list(map(addPoints, l1, l2))

for p in l1:
    print(p.showPoint())

print('---------------------------------------------')

for p in l2:
    print(p.showPoint())

l3.sort(key=lambda p: p.mag)

print('---------------------------------------------')

for p in l3:
    print(p.showPoint())