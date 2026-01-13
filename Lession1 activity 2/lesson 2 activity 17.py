class shape:
    def area(self):
        print("I am trying to run the area")

class rectangle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        print("The area is", self.l * self.b)

r = rectangle(5, 9)
r.area()

class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print("The area is", self.side * self.side)

s = square(5)
s.area()
        
