'''
Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
должен включать все файлы и подпапки исходного каталога
'''

import os
import zipfile


def zip_directory(source_dir, output_zip):
    """
    Создает архив .zip из указанного каталога.
    :param source_dir: Путь к исходному каталогу для архивирования.
    :param output_zip: Путь к целевому архиву .zip.
    """

    # Создаем объект ZipFile для записи архива
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Проходим по всем файлам и папкам в исходном каталоге
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Полный путь к текущему файлу
                file_path = os.path.join(root, file)
                # Добавляем файл в архив с путем относительно исходного каталога
                zipf.write(file_path, os.path.relpath(file_path, source_dir))




# Пример использования функции
zip_directory('/path/to/source_dir', '/path/to/output.zip')