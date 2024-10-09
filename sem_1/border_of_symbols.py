'''
Напишите программу, которая рисует прямоугольную рамку с помощью
символьной графики. Для вертикальных линий используйте символ
вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
высоту рамки определяет пользователь.
'''

SPACE = ' '
VERTICAL = '|'
HORISONTAL = '-'

height = int(input('Введите высоту: '))
width = int(input('Введите ширину: '))

for line in range(height + 1):
    for col in range(width + 1):
        if col == 0 or col == width:
            print(VERTICAL, end='')
        elif line == 0 or line == height:
            print(HORISONTAL, end='')
        else:
            print(SPACE, sep='', end='')
    print()