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
_____________________________________________________________________
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно
______________________________________________________________________
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
import os

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
    :param count_files: количество файлов, по умолчанию 2
    """

    while True:
        name = ''.join(choices(ascii_lowercase + digits + '_',
                k = randint(min_name, max_name)))
        name = f'{name}.{extension}'
        if not Path(name).is_file():
            break
    data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))

    with open(f'{name}.{extension}', 'wb') as file:
        file.write(data)

def file_generate(path: str | Path, **kwargs) -> None:
    """
    Генерирует указанное количество файлов указанных расширений
    :param **kwargs:
                    расширение=количество
    """
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    os.chdir(path)

    for ext, count in kwargs.items():
        files_maker(extension=ext, count_files=count)


if __name__ == '__main__':

    file_generate('C:\\Users\\chiffka\\Documents\\Python_deepening\\Files_and_Directories_(7)\\new_dir' , txt=3, jpg=2, bin=1)