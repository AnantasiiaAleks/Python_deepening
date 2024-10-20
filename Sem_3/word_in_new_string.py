'''
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
'''

text = input('Введите текст: ')
print('\n')

text_without_chars = (text.replace(',', '')
                      .replace('.', '')
                      .replace(' -', ''))
list_text = sorted(text_without_chars.split())
max_len = 0
for word in list_text:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
for num, word in enumerate(list_text, 1):
    print(f'{num} {word: >{max_len}}')