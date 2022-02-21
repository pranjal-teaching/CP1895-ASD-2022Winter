class Fraction:
    def __init__(self, numerator, denominator):
        self.__num = numerator
        self.__denom = denominator

    @property
    def numer(self):
        return self.__num

    @property
    def denom(self):
        return self.__denom

    # Hint
    # Create another property called decimal and just return num/denom
    # return self.decimal > other.decimal

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __add__(self, other):
        # must return a Fraction obj
        pass

    def __sub__(self, other):
        # must return a Fraction obj
        pass

    def __mul__(self, other):
        # must return a Fraction obj
        pass

    def __truediv__(self, other): # Correction -> div should have been truediv
        # must return a Fraction obj
        pass

    def __eq__(self, other):
        # Returns True/False
        pass

    def __lt__(self, other):
        # Returns True/False
        pass

    def __gt__(self, other):
        # Returns True/False
        pass

    def __le__(self, other):
        # Returns True/False
        pass

    def __ge__(self, other):
        # Returns True/False
        pass


two_thirds = Fraction(numerator=2, denominator=3)
half = Fraction(numerator=1, denominator=2)
print(two_thirds)
print(half)

# to test __add__
print(two_thirds / half)