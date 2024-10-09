'''
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы
'''

DOT = '.'

depth = int(input('Введите глубину ямы: '))

for line in range(depth):
    for left_number in range(depth, depth - line - 1, -1):
        print(left_number, end="")

    point_count = 2 * (depth - line - 1)
    print(DOT * point_count, end="")

    for right_number in range(depth - line, depth + 1):
        print(right_number, end="")

    print()