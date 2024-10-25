'''
По итогу в программе должны быть реализованы две функции:
1. maximum_of_two — функция принимает два числа и возвращает одно
(наибольшее из двух);
2. maximum_of_three — функция принимает три числа и возвращает одно
(наибольшее из трёх); при этом она должна использовать для сравнений
первую функцию maximum_of_two.
'''


def maximum_of_two(num1: int | float, num2: int | float) -> int | float:
    if num1 >= num2:
        return num1
    else:
        return num2


def maximum_of_three(num1: int | float, num2: int | float, num3: int | float) -> int | float:
    first_max = maximum_of_two(num1, num2)
    return maximum_of_two(first_max, num3)


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print(maximum_of_two(a, b))

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
print(maximum_of_three(x, y, z))