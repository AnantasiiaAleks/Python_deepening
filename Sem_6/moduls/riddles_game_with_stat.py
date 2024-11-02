'''
Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.
'''

__all__ = ['storage', 'print_stat_dict']

_stat_dict = {}

def stat_func(riddle: str, try_count: int) -> None:
    _stat_dict.update({riddle: try_count})


def riddle_game(text: str, answers: list, max_count: int=3) -> int:
    print(f'Отгадай загадку: {text}')
    for i in range(1, max_count + 1):
        player = input(f'Попытка номер {i}. Dаш ответ: ').lower()
        if player in answers:
            return i
    return 0


def storage():
    riddles = {
        'Без счёту одёжек и все без застёжек.': ['капуста'],
        'В воде искупался — сухим остался.': ['гусь'],
        'Не зверь, не птица.А нос — как спица.': ['комар'],
        'Ни окон, ни дверей — полна горница людей.': ['огурец'],
        'Сам худ, голова с пуд.': ['топор'],
        'Блещет в речке чистой спинкой серебристой.': ['рыба'],
        'Кто в речном песке живёт, ходит задом наперёд?': ['рак'],
        'Зелёная дорожка щекочет босые ножки.': ['трава']
    }
    for riddle, answ in riddles.items():
        res = riddle_game(riddle, answ)
        print(f'Угадал с {res} попытки' if res else 'Не угадал')
        stat_func(riddle, res)





def print_stat_dict():
    statistics = (
        f'Загадку "{riddle}" угадали с {count} попытки.' if count
        else f'Загадку "{riddle}" не угадали.'
        for riddle, count in _stat_dict.items()
    )
    print(*statistics, sep='\n')



if __name__ == '__main__':
    storage()
    print_stat_dict()
    # text = 'Висит груша, нельзя скушать'
    # answs = ['лампочка', 'грелка', 'чашка', 'кот']
    # res = riddle_game(text, answs, 5)
    # print(f'Угадал с {res} попытки' if res else 'Не угадал')