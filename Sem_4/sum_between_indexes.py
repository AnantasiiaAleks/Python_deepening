'''
Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
'''


def sum_btw_idxs(nums_list: list[int | float], start_idx: int, stop_idx: int) -> int | float:

    result = 0
    if stop_idx <= len(nums_list):
        for i in range(start_idx+1, stop_idx):
            result += nums_list[i]
    else:
        for i in range(start_idx+1, len(nums_list)+1):
            result += nums_list[i]
    return result

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(sum_btw_idxs(list_1, 2, 10))