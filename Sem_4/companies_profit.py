'''
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''


def company_profit(companies: dict[str, list[int]]) -> bool:

    for values in companies.values():
        sum_profit = 0
        sum_profit = sum(values)
        if sum_profit <= 0:
            return False
    return True

companies = {
    'Gazprom': [10, 10, 10, 10, -40],
    'Lukoil': [-40, -10, 30, 40],
    'Neftmagistral': [30, 40, 20, 100]
}
print(company_profit(companies))