class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

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

## Main Program
p1 = Point()
p2 = Point(3, -4)

p2.move(5,5)

print(p1.x, p1.y)
print(p2.x, p2.y)

