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

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass


two_thirds = Fraction(numerator=2, denominator=3)
half = Fraction(numerator=1, denominator=2)
print(two_thirds)
print(half)

# to test __add__
print(two_thirds + half)