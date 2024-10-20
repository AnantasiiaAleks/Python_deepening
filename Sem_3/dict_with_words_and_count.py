'''
Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
или не совпадают в ваших решениях.
'''

text = input('Введите текст: ')
text_without_chars = (text.replace(',', '')
                      .replace('.', '')
                      .replace(' -', '')
                      .replace(' ', '')
                      .lower())
char_dict = {}
#1
# for char in set(text_without_chars):
#     char_dict[char] = text.count(char)
#
# print(char_dict)

#2
# COUNT = 1
# for char in text_without_chars:
#     count = 1
#     if char not in char_dict:
#         char_dict[char] = COUNT
#     else:
#         char_dict[char] += 1
#
# print(char_dict)

#3
for char in text_without_chars:
    char_dict[char] = char_dict.get(char, 0) + 1

print(char_dict)