'''
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''
import json
from pathlib import Path

MIN_LEVEL = 1
MAX_LEVEL = 7


def set_users(user_file: Path) -> None:
    """

    """

    unique_id = set()
    if not user_file.is_file():
        data = {str(i): {} for i in range(MIN_LEVEL, MAX_LEVEL + 1)}
    else:
        with open(user_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
            for dict_level in data.values():
                unique_id.update(dict_level)
                print(f'{unique_id = }')

    while True:
        name = input('Enter name: ')
        if not name:
            break
        user_id = input('Enter id: ')
        level = input('Enter level from 1 to 7: ')
        while level not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Incorrect input. Try again...')
            level = input('Enter level from 1 to 7: ')
        if user_id not in unique_id:
            data[level].update({user_id: name})
            unique_id.add(user_id)
            with open(user_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    set_users(Path('users.json'))