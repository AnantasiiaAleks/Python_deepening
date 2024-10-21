'''
Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.
'''

list_1 = [1, 2, 2, 5, 4, 3, 3, 3, 6, 5, 9, 4]

duplicates = []

for elem in list_1:
    if list_1.count(elem) > 1 and elem not in duplicates:
        duplicates.append(elem)

print(f'{duplicates = }')