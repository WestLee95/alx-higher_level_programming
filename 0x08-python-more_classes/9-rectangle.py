#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self._Rectangle_width = self._validate_and_set_width(width)
        self._Rectangle_height = self._validate_and_set_height(height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @property
    def width(self):
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        self._Rectangle_width = self._validate_and_set_width(value)

    @property
    def height(self):
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        self._Rectangle_height = self._validate_and_set_height(value)

    def _validate_and_set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return value

    def _validate_and_set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return value

    def area(self):
        return self._Rectangle_width * self._Rectangle_height

    def perimeter(self):
        return 2 * (self._Rectangle_width + self._Rectangle_height) if
                    self._Rectangle_width > 0 and self._Rectangle_height > 0
                    else 0

    def __str__(self):
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return ""
        return '\n'.join([str(Rectangle.print_symbol) *
                          self._Rectangle_width for _ in range
                          (self._Rectangle_height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self._Rectangle_height,
                                          self._Rectangle_width)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
