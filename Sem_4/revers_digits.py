'''
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
каждое число на число, которое получается из исходного записью его цифр в
обратном порядке, затем складывает их, снова переворачивает и выводит
ответ на экран.
Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225
'''


def reverse_digit(num: int) -> int:

    num_str = str(num)
    reverse_str = num_str[::-1]
    return int(reverse_str)


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(f'Первое число наоборот: {reverse_digit(num1)}')
print(f'Второе число наоборот: {reverse_digit(num2)}')
sum_reverse_dig = reverse_digit(num1) + reverse_digit(num2)
print(f'Сумма: {sum_reverse_dig}')
print(f'Сумма наоборот: {reverse_digit(sum_reverse_dig)}')