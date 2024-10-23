'''
Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''
import random


def bubble_sort(nums_list: list[int | float]) -> list[int | float]:
    """Меняет местами соседние элементы до тех пор, пока не отсортирует весь массив"""

    n = len(nums_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_list[j] > nums_list[j + 1]:
                nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]
    return nums_list


def selection_sort(nums_list: list[int | float]) -> list[int | float]:
    """Массив просматривается справа налево и на каждую очередную позицию выбирается наименьший элемент O(N**2)"""

    n = len(nums_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if nums_list[j] < nums_list[min_index]:
                min_index = j

            nums_list[i], nums_list[min_index] = nums_list[min_index], nums_list[i]
    return nums_list


def merge_sort(nums_list: list[int | float]) -> list[int | float]:
    '''Сортировка слиянием:сортирова двух отрезков массива с последующим слиянием O(N*logN)'''

    aux = [None] * len(nums_list)

    def r_sort(lo, hi):
        if hi > lo:
            mid = (lo + hi) // 2
            r_sort(lo, mid)
            r_sort(mid+1, hi)
            merge(lo, mid, hi)

    def merge(lo, mid, hi):
        aux[lo:hi+1] = nums_list[lo:hi+1]
        left, right = lo, mid+1
        for i in range(lo, hi+1):
            if left > mid or right <= hi and aux[right] < aux[left]:
                nums_list[i] = aux[right]
                right += 1
            else:
                nums_list[i] = aux[left]
                left += 1
    r_sort(0, len(nums_list) - 1)
    return nums_list


def quick_sort(nums_list: list[int | float]) -> list[int | float]:
    """рекурсивный метод, опорный элемент, слева от него меньшие, справа - большие"""

    if len(nums_list) <= 1:
        return nums_list
    else:
        q = random.choice(nums_list)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums_list:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


array = [9, 7, 7, 9, 34, 56, 72, 3]
print(f'До сортировки {array = }')
print(bubble_sort(array))
print(selection_sort(array))
print(merge_sort(array))
print(quick_sort(array))
