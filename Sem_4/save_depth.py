'''
Напишите программу, находящую такое значение глубины х, при котором
уровень опасности как можно более близок к нулю. На вход программе
подаётся максимально допустимое отклонение уровня опасности от нуля, а
программа должна рассчитать приблизительное значение х, удовлетворяющее
этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
метров. Обеспечьте контроль ввода.
'''


def calculate_danger(x: int | float) ->int | float:
    return x**3 - 3*x**2 - 12*x + 10


def find_safe_depth(max_danger):
    depth_min = 0
    depth_max = 4
    depth_middle = (depth_min + depth_max) / 2
    middle_danger = calculate_danger(depth_middle)

    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            depth_min = depth_middle
        else:
            depth_max = depth_middle
        depth_middle = (depth_min + depth_max) / 2
        middle_danger = calculate_danger(depth_middle)
    return depth_middle

def main():
    """Основная функция для управления программой и ввода данных."""
max_danger = float(input('Введите допустимый уровень опасности: '))
if max_danger < 0:
    print('Вы ввели недопустимое значение! Попробуйте еще раз.')
else:
    safe_depth = find_safe_depth(max_danger)
    print(f'Приблизительная глубина безопасной кладки: {safe_depth:.9f} м')


main()