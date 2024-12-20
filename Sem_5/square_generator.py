'''
Пользователь вводит число N. Напишите программу, которая генерирует
последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
далее). Реализацию напишите двумя способами: функция-генератор и
генераторное выражение.
'''
LIMIT = 5

def generator_square(n):
    for num in range(1, n + 1):
        yield num ** 2


'''
Подсказка № 3
Реализуйте функцию-генератор, которое создайте генераторное выражение для
генерации квадратов чисел от 1 до n. Генераторное выражение имеет более
компактный синтаксис и создаётся внутри круглых скобок. Выведите сгенерированные
значения с помощью цикла for.'''

print(*generator_square(5))

print(*(
    num**2 for num in range(1, LIMIT + 1)
))