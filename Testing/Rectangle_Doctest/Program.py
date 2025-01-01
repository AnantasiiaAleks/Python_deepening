import doctest

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Не кукожьте!")
        self.width = width
        self.height = height

    def get_area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

    def get_perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2*(self.width+self.height)



if __name__=="__main__":
    doctest.testmod()