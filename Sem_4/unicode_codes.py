'''
Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''


def unicode_codes(text: str) -> list:
    """преобразует символы строки в коды Unicode"""


    unicode_list = []
    for char in text:
        unicode_list.append(ord(char))
    unicode_list.sort(reverse=True)
    return unicode_list


text = input('Введите строку: ')
print(unicode_codes(text))
