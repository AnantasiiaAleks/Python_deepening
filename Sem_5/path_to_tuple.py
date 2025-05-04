'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os

def path_to_tuple(text: str) -> tuple:
    path = os.path.dirname(text)          # путь до файла
    filename = os.path.splitext(os.path.basename(text))[0]  # имя файла без расширения
    extension = os.path.splitext(text)[1][1:]               # расширение без точки
    return (path, filename, extension)


text = input('Введите путь: ')
print(path_to_tuple(text))

