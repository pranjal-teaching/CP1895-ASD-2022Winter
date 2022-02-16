import turtle
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float
    color: str

    def draw(self, t):
        print(f"Circle with radius {self.radius} and color {self.color}")
        t.color(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()


@dataclass
class Rectangle:
    width: float
    height: float
    color: str

    def draw(self, t):
        print(f"Rectangle with width {self.width} and height {self.height} and color {self.color}")
        t.color(self.color)
        t.begin_fill()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.end_fill()


class Square(Rectangle):
    def __init__(self, side, color):
        Rectangle.__init__(self, side, side, color)

    def draw(self, t):
        print(f"Square with width {self.width} and height {self.height} and color {self.color}")
        t.color(self.color)
        t.begin_fill()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.end_fill()


c = Circle(radius=100, color="red")
r = Rectangle(width=50, height=80, color="blue")
s = Square(side=60, color="green")

bob = turtle.Turtle()
# c.draw(bob)
# r.draw(bob)
# s.draw(bob)



# create new class called Scene
# have the following methods: add_shape, __iter__
class Scene:
    def __init__(self):
        pass

    def add_shape(self, new_shape):
        pass

    def __iter__(self):
        pass

my_scene = Scene
my_scene.add_shape(c)
my_scene.add_shape(r)
my_scene.add_shape(s)

for shape in my_scene:
    shape.draw(bob)

turtle.done()