#!/usr/bin/python3
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    def width(self):
        return self.__width
    def width(self, value):
        if type(width) != 'int':
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def width(self):
        return self.__height
    def height(self, value):
        if type(height) != 'int':
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
