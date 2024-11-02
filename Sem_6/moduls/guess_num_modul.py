'''
Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
'''
from random import randint as rnd

__all__ = ['guess_my_number']


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
    print(guess_my_number(1, 100, 3))