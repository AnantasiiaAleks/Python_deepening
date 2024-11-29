'''
Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
JSON файл с другой структурой. CSV файл содержит данные о книгах (название,
автор, год издания). В JSON файле данные должны быть сгруппированы по
авторам, а книги каждого автора должны быть записаны как список.
'''

import csv
import json


def convert_csv_to_json(input_file, output_file):
    """

    """

    books_by_author = {} # Словарь для хранения книг по авторам

    with open(input_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }

            if author in books_by_author:
                books_by_author[author].append(book) # Добавляем книгу к существующему автору
            else:
                books_by_author[author] = [book] # Создаем новый список книг для нового автора


    # Запись данных в JSON файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(books_by_author, f, indent=4) # Сохраняем данные в JSON формате
