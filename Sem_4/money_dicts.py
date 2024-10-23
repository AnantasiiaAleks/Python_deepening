'''
Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
'''


def salary_calc(names: list[str], rate: list[int], bonus: list[str]) -> dict[str, float]:
    """Переводит бонусы в вещественное, считает деньги, делает словарь"""

    bonus_list = map(lambda s: float(s.replace('%', ''))/100, bonus)
    calc = [a*b for a, b in zip(rate, bonus_list)]
    return dict(zip(names, calc))


names = ['Nik', 'Stepan', 'Oleg']
rate = [100, 200, 300]
bonus = ['50%', '20%', '10%']

print(salary_calc(names, rate, bonus))
