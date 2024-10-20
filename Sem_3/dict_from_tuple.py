'''
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''

data = (1, 'HelloWorld!', 45.2, [2, 3, 6], True, 3, 'Privet', ['u', 'i'])

result = {}

for item in data:
    item_type = type(item)
    if item_type not in result:
        result[item_type] = [item]
    else:
        result[item_type].append(item)
print(result)