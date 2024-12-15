'''
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
'''
from typing import TextIO


def read_or_begin(fd: TextIO) -> str:
    text = fd.readline().strip()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text


def converte(digits_file: str, names_file: str, result_file: str) -> None:
    """
    - перемножает пары чисел из файла digits
    - изменяет регистр строки в файле names
    - записывает все в файл result
    :param digits_file: файл с парами чисел для перемножения
    :param names_file: файл со строками
    :param result_file: файл для записи результата
    """
    with (
        open(digits_file, 'r', encoding='utf-8') as dig_f,
        open(names_file, 'r', encoding='utf-8') as names_f,
        open(result_file, 'w', encoding='utf-8') as res_f
    ):
        len_digits = sum(1 for _ in dig_f)
        len_names = sum(1 for _ in names_f)
        for _ in range(max(len_names, len_digits)):
            dig_str = read_or_begin(dig_f)
            name = read_or_begin(names_f)
            num_1, num_2 = dig_str.split('|')
            mult = int(num_1) * float(num_2)
            if mult < 0:
                res_f.write(f'{name.lower()}|{abs(mult)}\n')
            else:
                res_f.write(f'{name.upper()}|{int(round(mult, 0))}\n')


converte('file_for_digits.txt', 'names.txt', 'result_file.txt')