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
        return f'Класс Rectangle {self.length=}, {self.width=}'


    def perimeter(self):
        """
        Метод, возвращающий периметр
        """
        return 2 * (self.length + self.width)

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
        a = self.length + other.length
        b = sum_perimeter / 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        """
        Вычитание периметров экземпляров
        """
        sub_perimeter = abs(self.perimeter() - other.perimeter())
        a = abs(self.length - other.length)
        b = sub_perimeter / 2 - a
        return Rectangle(a, b)

if __name__ == '__main__':
    rect1 = Rectangle(2, 5)
    rect2 = Rectangle(4)

    print(rect1.perimeter())
    print(rect2.perimeter())
    rect3 = rect1 + rect2
    print(rect3)
    rect4 = rect1 - rect2
    print(rect4)
    print()
    print(rect1.area())
    print(rect2.area())