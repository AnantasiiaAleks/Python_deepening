'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle. Для дочерних объектов указывайте родительскую директорию. Для
каждого объекта укажите файл это или директория. Для файлов сохраните его
размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами разных форматов.
'''
import os
import json
import csv
import pickle


def get_size(path):
    """
    Обходит директории, возвращает размер файла или директории
    """

    if os.path.isfile(path):
        return os.path.getsize(path)   # если файл - возвр. размер
    elif os.path.isdir(path):
        total_size = 0
        for dir_path, _, file_names in os.walk(path):
            for file_name in file_names:
                file_path = os.path.join(dir_path, file_name)
                total_size += os.path.getsize(file_path)
        return total_size


def inspect_dir(directory):
    """Рекурсивный обход директорий"""

    result = []
    for root, dirs, files in os.walk(directory):    # Обход директории с помощью os.walk,
        for name in dirs + files:                   #  который возвращает корневую директорию,
            path = os.path.join(root, name)         #  поддиректории и файлы
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)
            result.append(                          # Добавление информации о текущем объекте в список
                {
                    'name': name,
                    'path': path,
                    'type': 'directory' if is_dir else 'file',
                    'size': size,
                    'parent': parent
                }
            )
    return result


def save_to_json(data, file):
    """Сохранение в формат json"""

    with open(file, 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)


def save_to_csv(data, file):
    """Сохранение в формат csv"""

    with open(file, 'w', encoding='utf-8', newline='') as csv_f:
        csv_writer = csv.DictWriter(csv_f, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        csv_writer.writeheader()
        csv_writer.writerows(data)


def save_to_pickle(data, file):
    """Сохранение в формат pickle"""

    with open(file, 'wb') as pickle_f:
        pickle.dump(data, pickle_f)


def main_function(directory):
    """Основная функция для обхода директории и записи данных в файлы"""

    data = inspect_dir(directory)

    save_to_json(data, 'dirinfo.json')
    save_to_csv(data, 'dirinfo.csv')
    save_to_pickle(data, 'dirinfo.pkl')


if __name__ == '__main__':
    main_function(os.getcwd())