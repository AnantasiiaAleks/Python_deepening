'''
Напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке
'''

nums = [int(x) for x in input("Введите числа через пробел: ").split()]

max_num = nums[0]

for num in nums:
    num = int(num)
    if num > max_num:
        max_num = num

print(f'{max_num = }')