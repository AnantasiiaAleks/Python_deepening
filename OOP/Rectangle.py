'''

У класса должно быть два метода, возвращающие периметр
и площадь.


Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений.
Добавьте сравнение прямоугольников по площади
 Должны работать все шесть операций сравнения

'''

class Rectangle:
    """
    Класс прямоугольник.
    Класс должен принимать длину и ширину при создании экземпляра.
    Если при создании экземпляра передаётся только одна сторона,
    считаем что у нас квадрат.
    """
    def __init__(self, width, length = None):
        self.width = width
        if length:
            self.length = length
        else:
            self.length = width

    def __str__(self):
        return f'Прямоугольник со сторонами {self.length} и {self.width}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.length})'


    def perimeter(self):
        """
        Метод, возвращающий периметр
        """
        return int(2 * (self.length + self.width))

    def area(self):
        """
        Метод, возвращающий площадь
        """
        return self.length * self.width

    def __add__(self, other):
        """
        Сложение периметров экземпляров
        """
        sum_perimeter = self.perimeter() + other.perimeter()
        a = int(self.length + other.length)
        b = int(sum_perimeter / 2 - a)
        return Rectangle(a, b)

    def __sub__(self, other):
        """
        Вычитание периметров экземпляров
        """
        sub_perimeter = abs(self.perimeter() - other.perimeter())
        a = int(abs(self.length - other.length))
        b = int(sub_perimeter / 2 - a)
        return Rectangle(a, b)

    def __lt__(self, other):
        """Сравнение по площади.
        Возвращает True если первый прямоугольник меньше"""
        return True if self.area() < other.area() else False

    def __eq__(self, other):
        """Сравнение по площади.
        Возвращает True площади равны"""
        return True if self.area() == other.area() else False

    def __le__(self, other):
        """Сравнение по площади.
            Возвращает True, если площадь первого прямоугольника
            меньше или равна площади второго, иначе False"""
        return True if self.area() <= other.area() else False


if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")
    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
    print(rect3)
    print(repr(rect4))