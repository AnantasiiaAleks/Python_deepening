'''
Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
'''
_month_31 = (1, 3, 5, 7, 8, 10, 12)
_month_30 = (4, 6, 9, 11)
_month_feb = 2


__all__ = ['date_check']

def date_check(input_date: str) -> bool:
    day, month, year = map(int, input_date.split('.'))
    if 1 <= year <= 9999:
        if month in _month_31 and 1 <= day <= 31:
            return True
        elif month in _month_30 and 1 <= day <= 30:
            return True
        elif month == 2:
            if _is_leap(year) and 1 <= day <= 29:
                return True
            elif 1 <= day <= 28:
                return True
    return False


def _is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
        else:
            return False
    else:
        return True
    return False


if __name__ == '__main__':
    date_input = input('Введите дату строкой вида DD.MM.YYYY: ')
    print(date_check(date_input))