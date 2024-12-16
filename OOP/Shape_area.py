from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Абстрактный базовый класс
    """

    @abstractmethod
    def area(self):
        """
        Абстрактный метод, который будет реализован в конкретных наследниках
        """
        pass


class Circle(Shape):
    """
    Класс-наследник
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2



class Rectangle(Shape):
    """Класс-наследник"""
    def __init__(self, length, width = None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def area(self):
        return self.length * self.width



class Triangle(Shape):
    """Класс-наследник"""
    def __init__(self, line, height):
        self.line = line
        self.height = height

    def area(self):
        return 0.5 * self.line * self.height



if __name__ == '__main__':
    circle = Circle(10)
    rect1 = Rectangle(2, 3)
    rect2 = Rectangle(4)
    tri = Triangle(4, 2)

    print(f'{circle.area()=}')
    print(f'{rect1.area()=}')
    print(f'{rect2.area()=}')
    print(f'{tri.area()=}')