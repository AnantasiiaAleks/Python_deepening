import random



NIRVANA_KARMA = 500                             # Константа для достижения просветления


class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Авария")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Обжорство")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("Уныние")



def one_day():
    """Один день из жизни"""

    day_karma = random.randint(1,7)           # Случайное количество кармы от 1 до 7
    if random.randint(1,10) == 5:             # Случайная вероятность выброса исключения
        exception = random.choice([KillError(), DrunkError(),
                            CarCrashError(), GluttonyError(), DepressionError()])
        raise exception                             # Случайный выбор исключения
    return day_karma


def main():
    """Омновная функция"""
    karma = 0

    with open('karma.log', 'w', encoding ='utf-8') as fl_logger:      # файл для записи логов
        while True:
            try:
                karma += one_day()              # Прибавляем карму за один день
            except Exception as ex:
                fl_logger.write(f'{ex}\n')      # Записываем информацию об исключении в файл
            if karma >= NIRVANA_KARMA:          # Достигнуто ли необходимое количество кармы
                break


    print('Вы достигли Нирваны!')
    print('Омм')



if __name__ == "__main__":
    main()
