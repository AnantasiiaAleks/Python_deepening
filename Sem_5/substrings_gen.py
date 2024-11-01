'''
Напишите генераторную функцию substrings(s), которая принимает строку
s и возвращает генератор всех возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
a
ab
abc
b
bc
c

'''

def substrings(s):
    """
    Генератор всех возможных подстрок строки s.
    :param s: Строка, из которой будут извлекаться подстроки
    :return: Генератор подстрок
    """

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            yield s[start:end]

for substring in substrings('abc'):
    print(substring)