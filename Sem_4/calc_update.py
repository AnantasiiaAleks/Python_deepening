'''
Напишите программу, запрашивающую у пользователя число и действие,
которое нужно сделать с числом: вывести сумму его цифр, максимальную или
минимальную цифру. Каждое действие оформите в виде отдельной функции, а
основную программу зациклите.
'''


def num_to_str(num: int | float) -> str:
    """переводит число в строку для последующей итерации"""

    num_str = ''
    if type(num) is int:
        num_str = str(num)
    elif type(num) is float:
        num_str = str(num).replace('.', '')
    return num_str


def sum_digits(num: int | float) -> int:
    """Вычисляет сумму цифр числа"""

    result = 0
    num_str = num_to_str(num)
    for char in num_str:
        result += int(char)
    return result


def find_max_digit(num: int | float) -> int:
    """Поиск максимальнй цифры в числе"""

    num_str = num_to_str(num)
    max_digit = int(num_str[0])
    for char in num_str:
        if int(char) > max_digit:
            max_digit = int(char)
    return max_digit

def find_min_digit(num: int | float) -> int:
    """Поиск минимальной цифры в числе"""

    num_str = num_to_str(num)
    min_digit = int(num_str[0])
    for char in num_str:
        if int(char) < min_digit:
            min_digit = int(char)
    return min_digit


while True:
    num = input("Введите число: ")
    if num.isdigit():
        num = int(num)
    elif num.replace('.', '').replace('-', '').isdigit()\
        and num.count('.') < 2 and '-' not in num[1:]:
        num = float(num)
    else:
        print('Неправильный ввод')
        break

    command = int(input("Введите номер операции:\n"
                        "1 - сумма цифр числа\n"
                        "2 - поиск максимальной цифры\n"
                        "3 - поиск минимальной цифры\n"
                        "\t\t\t:"))
    match command:
        case 1:
            print(sum_digits(num))
        case 2:
            print(find_max_digit(num))
        case 3:
            print(find_min_digit(num))