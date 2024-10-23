'''
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
'''


def words_to_new_string(text):
    """Разбить строку на слова и каждое вывести на новой строке"""

    str_without_chars = (text.replace(',', '')
                         .replace('.', '')
                         .replace(' -', ''))
    list_str = sorted(str_without_chars.split())
    max_len = 0
    for word in list_str:
        word_len = len(word)
        if word_len > max_len:
            max_len = word_len
    words_dict = {}
    for num, word in enumerate(list_str, 1):
        print(f'{num:>2} {word: >{max_len}}')


text = input('Введите строку: ')
words_to_new_string(text)
