#!/usr/bin/python3
class Rectangle:
    def __init__(self, height=0, width=0):
        self._Rectangle_height = self._validate_and_set_height(height)
        self._Rectangle_width = self._validate_and_set_width(width)

    @property
    def height(self):
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        self._Rectangle_height = self._validate_and_set_height(value)

    @property
    def width(self):
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        self._Rectangle_width = self._validate_and_set_width(value)

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
        return 2 * (self._Rectangle_width + self._Rectangle_height)
    if self._Rectangle_width > 0 and self._Rectangle_height > 0 else 0
