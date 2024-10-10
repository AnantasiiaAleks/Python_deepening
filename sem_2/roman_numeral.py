'''
Программа принимает целое число и возвращает его римское представление в
виде строки
'''

num = int(input("Введите целое число: "))

decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanian = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

roman_num = ''
i = 0

while num > 0:
    for _ in range(num // decimals[i]):
        roman_num += romanian[i]
        num -= decimals[i]
    i += 1

print("Результат:", roman_num)
