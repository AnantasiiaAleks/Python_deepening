'''
Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''
import random
from pathlib import Path


MIN_LENGTH = 4
MAX_LENGTH = 7
VOVELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def names_generator(count: int, file_name: str | Path) -> None:
    """
    Генерирует случайные строки из букв.
    Имя начинается с заглавной буквы, должно содержать хотя бы одну гласную букву
    """
    for _ in range(count):
        first_char = random.choice([-1, 1])
        name = ''
        for _ in range(random.randint(MIN_LENGTH, MAX_LENGTH)):
            if first_char == -1:
                name += random.choice(CONSONANTS)
            else:
                name += random.choice(VOVELS)
            first_char *= -1
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f'{name.capitalize()}\n')


names_generator(4, 'names.txt')
