class Matrix:
    """
    Класс Matrix для работы с матрицами
    с инициализацией матрицы с нулями
    """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        """Сложение матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Размеры матриц не совпадают')
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res

    def __sub__(self, other):
        """Вычитание матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Размеры матриц не совпадают')
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.data[i][j] - other.data[i][j]
        return res

    def __mul__(self, other):
        """Умножение матриц"""
        if self.cols != other.rows:
            raise ValueError('Количество столбцов первой матрицы должно совпадать с количеством строк второй')
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res.data[i][j] += self.data[i][k] * other.data[k][j]
        return res

    def transpose(self):
        """
        Транспонирование матрицы
        """
        res = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[j][i] = self.data[i][j]
        return res


    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


matr1 = Matrix(2, 3)
matr1.data = [[1, 2, 3], [4, 5, 6]]
matr2 = Matrix(2, 3)
matr2.data = [[7, 8, 9], [10, 11, 12]]
print(matr1)
print(matr2)
print()
#print(print(matr1.add(matr2)))
add_matr = matr1 + matr2
sub_matr = matr1 - matr2
trans_matr = matr1.transpose()
mul_matr = matr2 * trans_matr

print(add_matr)

print()
print(sub_matr)
print()
print(trans_matr)
print()
print(mul_matr)