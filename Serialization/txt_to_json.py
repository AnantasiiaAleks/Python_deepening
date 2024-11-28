'''
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

import json
from pathlib import Path


def convert_to_json(input_file: Path) -> None:
    """
    создаёт из созданного ранее файла новый с данными в формате JSON.
    Имена с большой буквы. Каждая пара - с новой строки.
    :param input_file: Файл с текстом
    """

    data = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            name, number = line.strip().split('|')
            data[name.strip().capitalize()] = float(number)


    with open(input_file.stem + '.json', 'w', encoding='utf-8') as out_file:
        json.dump(data, out_file, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_json(Path('result.txt'))