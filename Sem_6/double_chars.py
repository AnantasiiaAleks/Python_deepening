'''
Напишите модуль с функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами. Например, строка
"aabbccaa" должна быть преобразована в "abca".
'''

def remove_duplicate_chars(text: str) -> str:
    """функция принимает строку и возвращает строку с удаленными дублирующимися
    подряд идущими символами"""

    chars_list = []
    if len(text) == 0:
        return text
    else:
        chars_list.append(text[0])
        for char in text[1:]:
            if char != chars_list[-1]:
                chars_list.append(char)
    return ''.join(chars_list)


if __name__ == '__main__':
    print(remove_duplicate_chars('aabbccca'))