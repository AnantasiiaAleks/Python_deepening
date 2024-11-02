import random


def are_queens_safe(positions):
    """
    Проверяет, не бьют ли друг друга ферзи на доске 8x8.
    Аргументы: positions -- список кортежей, где каждый кортеж содержит
    координаты ферзя (строка, столбец)
    Возвращает: True, если ферзи не бьют друг друга; False в противном случае
    """
    def is_under_attack(row, col):
        """
        Проверяет, атакуется ли позиция (row, col) другими ферзями.
        Аргументы:
        row -- строка ферзя
        col -- столбец ферзя
        Возвращает:
        True, если позиция находится под атакой; False в противном
        случае
        """
        for i in range(8):
            if i != row:
            # Проверяем по столбцам и диагоналям
                if (positions[i][1] == col or
                abs(positions[i][0] - row) == abs(positions[i][1] - col)):
                    return True
            return False
        for i in range(8):
            if is_under_attack(positions[i][0], positions[i][1]):
                return False
        return True


def generate_random_queens_placement():
    """
    Генерирует случайную расстановку 8 ферзей.
    Возвращает:
    Список из 8 кортежей, каждый из которых содержит случайные координаты ферзя
    """

    return [(i, random.randint(1, 8)) for i in range(8)]


def print_valid_placements(num_placements=4):
    """
    Выводит заданное количество случайных валидных расстановок ферзей.
    Аргументы:
    num_placements -- количество случайных валидных расстановок для вывода
    """
    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            print(placement)
            count += 1