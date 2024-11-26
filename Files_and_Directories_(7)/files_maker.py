'''
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 2
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''

from random import randint, choices
from string import ascii_lowercase, digits

def files_maker(extension: str = 'txt', min_name: int = 6,
                max_name: int = 30, min_size: int = 256,
                max_size: int = 4096, count_files: int = 2) -> None:
    """
    создаёт файлы с указанным расширением
    :param extension: расширение
    :param min_name: минимальная длина случайно сгенерированного имени, по умолчанию 6
    :param max_name: максимальная длина случайно сгенерированного имени, по умолчанию 30
    :param min_size: минимальное число случайных байт, записанных в файл, по умолчанию 256
    :param max_size: максимальное число случайных байт, записанных в файл, по умолчанию 4096
    :param count_files: количество файлов, по умолчанию 42
    """

    for _ in range(count_files):
        name = ''.join(choices(ascii_lowercase + digits + '_',
                k = randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

        with open(f'{name}.{extension}', 'wb') as file:
            file.write(data)


files_maker()