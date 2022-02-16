# 15-2 Porject rectangle or square calculator

class Rectangle:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)

    def make_shape(self):
        column_counter = 0
        row_counter = 1

        while row_counter <= self.__height:
            if row_counter == 1 or row_counter == self.__height:
                print("*  " * self.__width)
            row_counter += 1
            if 1 < row_counter < self.__height:
                print("*  " + ("   " * (self.__width - 2)) + "*")

    def __str__(self):
        result = ''

        row_counter = 1
        while row_counter <= self.__height:
            if row_counter == 1 or row_counter == self.__height:
                result += ("*  " * self.__width) + '\n'
            row_counter += 1
            if 1 < row_counter < self.__height:
                result += ("*  " + ("   " * (self.__width - 2)) + "*") + '\n'

        return result

class Square(Rectangle):
    def __init__(self, height):
        Rectangle.__init__(self, height, height)


def main():
    print("Rectangle Calculator\n")
    shape = input("Rectangle or Square? (r/s): ")
    height = int(input("Height: "))

    if shape == "s":
        my_sq = Square(height)
        print(my_sq)
    elif shape == "r":
        width = int(input("Width: "))
        my_rect = Rectangle(height, width)
        print(my_rect)
        print('Here comes make_shape')
        my_rect.make_shape()

    # rec1 = Rectangle(height, width)
    # print(rec1)


if __name__ == "__main__":
    main()
