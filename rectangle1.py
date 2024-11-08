class Rectangle:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    def area(self):
        return self.__width * self.__length

    def perimeter(self):
        return 2 * (self.__width + self.__length)


def main():
    values = Rectangle(100, 50)
    print(f"Rectangle's width and length: {values.width}, {values.length}")
    print(f"Rectangle's area: {values.area()}")
    print(f"Rectangle's perimeter: {values.perimeter()}")
    values.width = 150
    values.length = 200
    print(f"Rectangle's width and length: {values.width}, {values.length}")
    print(f"Rectangle's area: {values.area()}")
    print(f"Rectangle's perimeter: {values.perimeter()}")


if __name__ == '__main__':
    main()