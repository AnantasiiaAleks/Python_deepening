'''
Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


def unicode_dict(nums: str) -> dict[str, int]:

    num1, num2 = map(int, nums.split())
    result = {}
    for num in range(min(num1, num2), max(num1, num2)):
        result[chr(num)] = num
    return result


numbers = input('Введите два числа через пробел: ')
print(unicode_dict(numbers))
