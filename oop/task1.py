class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

## Main Program
p1 = Point()
p2 = Point(3, -4)

print(p1.x, p1.y)
print(p2.x, p2.y)