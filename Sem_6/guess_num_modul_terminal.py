'''
Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
'''

from random import randint as rnd
from sys import argv


def guess_my_number(min_value: int=0, max_value: int=100, attempt: int=10) -> bool:
    number = rnd(min_value, max_value + 1)
    count = 0
    for _ in range(attempt):
        player = int(input('Введите число: '))
        if player < number:
            print('Слишком мало')
            count += 1
        elif player > number:
            print('Слишком много')
            count += 1
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    params = (int(num) for num in argv[1:])
    print(guess_my_number(*params))