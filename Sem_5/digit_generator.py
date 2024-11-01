'''
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
'''

# def even_numbers_gen(limit):
#
#     for num in range(0, limit+1, 2):
#         if num % 10 + num // 10 != 8:
#             yield num
#
# print(list(even_numbers_gen(100)))

even_num = (num for num in range(0, 100 + 1, 2) if num % 10 + num // 10 != 8)
print(*even_num)