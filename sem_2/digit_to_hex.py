'''
Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление. Функцию hex используйте для
проверки своего результата.
'''
from math import remainder

num = int(input('Введите число: '))

hex_digits = '0123456789ABCDEF'

if num == 0:
    hex_string = '0'
else:
    # Обрабатываем отрицательные числа
    is_negative = num < 0
    if is_negative:
        num = -num
    # Преобразование числа в шестнадцатеричное представление
    hex_string = ''
    while num > 0:
        remainder = num % 16
        hex_string = hex_digits[remainder] + hex_string
        num //= 16
    hex_string = '0x' + hex_string
    if is_negative:
        hex_string = '-' + hex_string

print(hex_string)