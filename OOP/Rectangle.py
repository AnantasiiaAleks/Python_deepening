'''
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''

class Rectangle:

    def __init__(self, width, length = None):
        self.width = width
        if length:
            self.length = length
        else:
            self.length = width


    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


if __name__ == '__main__':
    rect1 = Rectangle(2, 4)
    rect2 = Rectangle(4)

    print(rect1.perimeter())
    print(rect2.perimeter())
    print()
    print(rect1.area())
    print(rect2.area())