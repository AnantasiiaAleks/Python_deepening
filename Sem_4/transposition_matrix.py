'''
Напишите функцию для транспонирования матрицы
'''
import numpy as np

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# transpose_matrix = np.transpose(matrix)
# print(transpose_matrix)



def transpose(matrix: list) -> list:
    """
    Транспонирование матрицы
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


transpose_matrix = transpose(matrix)
for row in transpose_matrix:
    print(row)


