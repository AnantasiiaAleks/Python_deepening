'''
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
'''

import json
import pickle
from pathlib import Path


def json_to_pickle(path: Path) -> None:
    """

    """

    for obj in path.iterdir():
        if obj.is_file() and path.suffix == '.json':
            with open(obj, 'r', encoding='utf-8') as f_r:
                data = json.load(f_r)
            with open(f'{obj.stem}.pkl', 'wb') as f_w:
                pickle.dump(data, f_w)

if __name__ == '__main__':
    print(Path.cwd())
    json_to_pickle(Path.cwd())