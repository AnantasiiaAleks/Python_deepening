'''
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''
from random import randint, uniform


MIN_DIGIT = -1000
MAX_DIGIT = 1000


def random_digits(min_value, max_value, n):
    """
    Создает список пар чисел. Первое число int, второе - float разделены вертикальной чертой.
    :param min_value: минимальное число
    :param max_value: максимальное число
    :param n: длина выходного списка
    """

    list_digits = []
    for i in range(n):
        list_digits.append(f'{randint(min_value, max_value + 1)}|{uniform(min_value, max_value + 1)}')

    with open('file_for_digits.txt', mode='a', encoding='utf-8') as f:
        for item in list_digits:
            f.write(f'{item}\n')
        print('Запись в файл произведена')


random_digits(MIN_DIGIT, MAX_DIGIT, 1)

#178|839.5201015580719
