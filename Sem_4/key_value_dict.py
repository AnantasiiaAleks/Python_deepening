'''
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''

def foo(**kwargs):
    result = {}
    for name, value in kwargs.items():
        try:
            hash(value)
            key = value
        except TypeError:
            key = str(value)
        result[key] = name
    return result

print(foo(a=1, b=[1, 2], c='hello world'))


