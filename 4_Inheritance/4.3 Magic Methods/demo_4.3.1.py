class ImperialDistance:
    def __init__(self, feet, inches):
        assert inches < 12, 'Inches must be less than 12'
        self.__feet = feet
        self.__inches = inches

    @property
    def feet(self):
        return self.__feet

    @property
    def inches(self):
        return self.__inches

    def __str__(self):
        return f'{self.__feet} feet and {self.__inches} inches'

    def __add__(self, other):
        total_feet = 0
        total_inches = self.inches + other.inches
        if total_inches >= 12:
            total_feet += 1
            total_inches -= 12
        total_feet += self.feet + other.feet
        return ImperialDistance(feet=total_feet, inches=total_inches)

    def __sub__(self, other):
        pass

    def __eq__(self, other):
        """
        Logic which determines the two objects are equal
        """
        return self.feet == other.feet and self.inches == other.inches

d1 = ImperialDistance(feet=3, inches=6)
d2 = ImperialDistance(feet=2, inches=9)
d3 = ImperialDistance(feet=3, inches=6)

# print(d1 + d2)
# print(d1 - d2)
print(d1 == d2)
print(d1 == d1)
print(d1 == d3)

d1 + d2