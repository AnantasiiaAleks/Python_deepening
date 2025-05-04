'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне [1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
from sys import argv

_month_31 = (1, 3, 5, 7, 8, 10, 12)
_month_30 = (4, 6, 9, 11)



__all__ = ['date_check']

def date_check(input_date: str) -> bool:
    '''
    Проверяет валидность введенной даты по Григорианскому календарю
    >>> python date_modul.py 29.02.2024
        True
    >>> python date_modul.py 31.06.2025
        False
    '''
    try:
        day, month, year = map(int, input_date.split('.'))
    except ValueError:
        return False    # Если введен некорректный формат даты

    if not (1 <= year <= 9999):
        return False
    if not (1 <= month <= 12):
        return False

    if month in _month_31:
        return  1 <= day <= 31
    elif month in _month_30:
        return 1 <= day <= 30
    elif month == 2:
        if _is_leap(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28

    return False


def _is_leap(year):
    """
    По Григорианскому календарю: если год делится на 400
    или делится на 4, но не на 100, год считается високосным
    """
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))


if __name__ == '__main__':
    if len(argv) != 2:
        print('Использование: python date_modul.py DD:MM:YYY')
    else:
        date_input = argv[1]
        print(date_check(date_input))