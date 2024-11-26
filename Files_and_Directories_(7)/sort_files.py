'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
from pathlib import Path


# def sort_files(source_dir):
#     """
#
#     """
#
#     video_ext = ['.mp4', '.mov', '.mkv']
#     image_ext = ['.png', '.jpg', '.jpeg']
#     text_ext = ['.txt', '.doc', '.pdf']
#
#     for file in os.listdir(source_dir):
#         if os.path.isfile(os.path.join(source_dir, file)):
#             file_ext = os.path.splitext(file)[1]
#
#             if file_ext in video_ext:
#                 dest_folder = os.path.join(source_dir, 'Videos')
#             elif file_ext in image_ext:
#                 dest_folder = os.path.join(source_dir, 'Images')
#             elif file_ext in text_ext:
#                 dest_folder = os.path.join(source_dir, 'Docs')
#             else:
#                 dest_folder = os.path.join(source_dir)

def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    os.chdir(path)
    if groups is None:
        groups = {
            Path('Videos'): ['mp4', 'mov', 'mkv'],
            Path('Images'): ['png', 'jpg', 'jpeg'],
            Path('Docs'): ['txt', 'doc', 'docx']
        }
    reverse_groups = {}
    for target_dir, ext_lst in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True)
        for ext in ext_lst:
            reverse_groups[f'.{ext}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(
                reverse_groups[file.suffix] / file.name
            )