'''
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
from math import pi


class Circle:


    def __init__(self, radius):
        self.radius = radius


    def circumference(self):
        return round(2 * self.radius * pi, 2)

    def circle_area(self):
        return round(pi * self.radius ** 2, 2)


if __name__ == '__main__':

    circle1 = Circle(3)
    print(f'{circle1.circumference()}')
    print(f'{circle1.circle_area()}')