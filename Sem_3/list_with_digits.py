'''
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
'''

list_1 = [1, 3, 5, 7, 3, 28, 1, 7, 4]
print(f'{list_1 = }')
list_2 = list(set(list_1))
print(f'{list_2 = }')

list_3 = []
for item in list_1:
    if item not in list_3:
        list_3.append(item)
print(f'{list_3 = }')

list_4 = sorted(list_1)
for i in range(len(list_4) - 1, 0, -1):
    if list_4[i] == list_4[i - 1]:
        del list_4[i]
print(f'{list_4 = }')