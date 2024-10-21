'''
Напишите программу, которая принимает два слова и определяет, являются ли
они анаграммами.
'''

words = input('Введите два слова через пробел: ').split()
dict_1 = {}
dict_2 = {}

if len(words[0]) != len(words[1]):
    print('Не могут быть анаграммами')
else:
    for char in words[0]:
        dict_1[char] = words[0].count(char)
    for char in words[1]:
        dict_2[char] = words[1].count(char)
    if dict_1 == dict_2:
        print('Слова являются анаграммами')
    else:
        print('Слова не являются анаграммами')