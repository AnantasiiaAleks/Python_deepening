import os
import logging
import argparse
from argparse import ArgumentParser
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name','ext', 'is_directory', 'parent_directory'])

logging.basicConfig(filename='os_structure.log', format='%(asctime)s. %(msg)s', level=logging.INFO, encoding='UTF-8')


def directories_info(dir_path):
    """

    """

    if not os.path.isdir(dir_path):
        raise ValueError('Не является папкой')

    parent_dir = os.path.basename(os.path.abspath(dir_path))

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            file_info = FileInfo(name=item, ext=None, is_directory=True, parent_directory=parent_dir)
        else:
            name, ext = os.path.splitext(item)
            file_info = FileInfo(name=name, ext=ext.lstrip('.'), is_directory=False, parent_directory=parent_dir)


        logging.info(f'{file_info.name} *** {file_info.ext if file_info.ext else "None"} ***'
                     f'{"Папка" if file_info.is_directory else "Файл"} *** {file_info.parent_directory}')


if __name__ == '__main__':

    parser = ArgumentParser(description='Сборщик информации о содержимом папки и запись в лог')
    parser.add_argument('directory', type=str, help='Путь до папки')
    args = parser.parse_args()
    directory_path = args.directory

    try:
        directories_info(directory_path)
    except ValueError as e:
        print(e)