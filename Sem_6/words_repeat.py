'''
Создайте модуль с функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке.
'''



def words_repeat(words: list) -> dict:

    """Функция получает список слов и возвращает словарь, в котором ключи —
    это слова, а значения — количество их повторений в списке."""

    repeat_dict = {}
    for word in words:
        repeat_dict[word] = repeat_dict.get(word, 0) + 1
    return repeat_dict


if __name__ == '__main__':
    print(words_repeat(['banana', 'apple', 'banana', 'pineapple', 'apple', 'banana']))