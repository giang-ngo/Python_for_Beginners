import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    def __str__(self):
        return f'Shape: x={self.__x}, y={self.__y}'


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f'Rectangle: width={self.__width}, height={self.__height}, ' \
               f'area={self.calculate_area()}, ' \
               f'perimeter={self.calculate_perimeter()}'


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__r = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__r

    def __str__(self):
        return f'Circle: r={self.__r}, perimeter={self.calculate_perimeter()}'


rect = Rectangle(width=20, height=40, x=9, y=0)
print(rect)
circle = Circle(radius=30, x=434, y=434)
print(circle)
