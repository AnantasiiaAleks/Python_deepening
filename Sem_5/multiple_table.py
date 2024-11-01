'''
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
'''

LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4

table = (
    f'{first_num:>2} * {second_num:>2} = {first_num * second_num:>2}\t' if first_num != main_row + COLUMN - 1 else
    f'{first_num:>2} * {second_num:>2} = {first_num * second_num:>2}\n' if second_num != UP_LIMIT else
    f'{first_num:>2} * {second_num:>2} = {first_num * second_num:>2}\n\n'
    for main_row in (LOW_LIMIT, LOW_LIMIT + COLUMN)
    for second_num in range(LOW_LIMIT, UP_LIMIT + 1)
    for first_num in range(main_row, main_row + COLUMN)
)

print(*table)