class Circle:
    def __init__(self, circle_radius, circle_colour):
        self.__radius = circle_radius  # Private data attr
        self.colour = circle_colour    # Public data attr

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        assert isinstance(new_radius, (int, float)), 'new radius must be an int or a float'
        assert new_radius > 0, 'new radius must be greater than 0'
        self.__radius = new_radius



my_circle = Circle(10, 'red')

print(my_circle.colour)  # prints red
# print(my_circle.__radius) # err
# print(my_circle.radius) # err
my_circle.set_radius(10.1)
print(my_circle.get_radius()) # prints 10
