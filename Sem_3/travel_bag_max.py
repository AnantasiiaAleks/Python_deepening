'''
4. Создайте словарь со списком вещей для похода в качестве ключа
и их массой в качестве значения. Определите какие вещи влезут в рюкзак,
передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''
from itertools import combinations

gear = {
    'Спальный мешок': 1500,
    'палатка': 6000,
    'Коврик': 600,
    'термобельё': 300,
    'брюки': 350,
    'носки': 150,
    'кепка': 60,
    'куртка': 500,
    'дождевик': 250,
    'сапоги': 600,
    'удочки': 1500,
    'крупа': 900,
    'тушенка': 350,
    'суп': 450,
    'горелка': 500,
    'котелок': 250,
    'сухое топливо': 300,
    'Средства гигиены': 150,
    'книги': 1300,
    'мобильный телефон': 350,
    'перекус': 550,
    'запас воды': 3000,
    'Фотоаппарат': 3000
}

bag_capacity = 15000

items = list(gear.items())

def find_one_pack(items, capacity):
    for r in range(len(items), 0, -1):
        for combo in combinations(items, r):
            total_weight = sum(item[1] for item in combo)
            if total_weight <= capacity:
                return [item[0] for item in combo], total_weight
    return [], 0

pack, weight = find_one_pack(items, bag_capacity)
print(f'Выбранные вещи (общий вес {weight} г): {pack}')


def find_valid_packs(items, capacity):
    pack_combinations = dict()
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            total_weight = sum(item[1] for item in combo)
            if 13000 <= total_weight <= capacity:
                # Для каждого веса кладём список вариантов, чтобы не перезаписывать
                if total_weight not in pack_combinations:
                    pack_combinations[total_weight] = []
                pack_combinations[total_weight].append([item[0] for item in combo])
    return pack_combinations

pack_combs = find_valid_packs(items, bag_capacity)
for weight, packs in pack_combs.items():
    for pack in packs:
        print(f'Выбранные вещи (общий вес {weight} г): {pack}')