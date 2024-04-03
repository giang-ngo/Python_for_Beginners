import math


class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calculate_peremiter(self):
        return 0

    def calculate_area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def calculate_peremiter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.r = radius

    def calculate_area(self):
        return math.pi * self.r ** 2

    def calculate_peremiter(self):
        return 2 * math.pi * self.r


rectangle = Rectangle(20, 30)
circle = Circle(100)
print(f'Chu vi hình chữ nhật: {rectangle.calculate_peremiter()}')
print(f'Diện tích hình chữ nhật: {rectangle.calculate_area()}')
print(f'Chu vi hình tròn: {circle.calculate_peremiter()}')
print(f'Diện tích hình tròn: {circle.calculate_area()}')
