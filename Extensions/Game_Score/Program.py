SCORE_LIMIT = 1000

class GameScore:
    """Класс для отслеживания очков игрока."""

    def __init__(self):
        self.score = 0              # Начальное значение очков

    def add_score(self, points):
        """Добавляет очки к текущему счету, проверяя лимит."""
        if self.score + points > SCORE_LIMIT:
            raise ScoreLimitExceededError()
        self.score += points


    def subtract_score(self,points):
        """Уменьшает очки, проверяя, чтобы счет не стал отрицательным."""
        if self.score-points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points

    def run(self):
        """Запускает основной цикл программы."""
        while True:
            print("Чтобы прибавить очки, нажмите 1, чтобы вычесть очки, введите 2, для выхода введите 0")
            answer = input("Введите 1 или 2: ")
            if answer == '1':
                try:
                    add_points = int(input('Введите количество очков: '))
                    self.add_score(add_points)
                    print(f"Текущий счет: {self.score}")
                except ScoreLimitExceededError as e:
                    print(e)
            elif answer == '2':
                try:
                    del_points = int(input('Введите количество очков: '))
                    self.subtract_score(del_points)
                    print(f"Текущий счет: {self.score}")
                except ValueError as e:
                    print(e)
            elif answer == '0':
                exit()
            else:
                print("Неизвестная команда\n")

class ScoreLimitExceededError(Exception):
    """Исключение, выбрасываемое при попытке добавить очки, превышающие лимит."""

    def __init__(self):
        super().__init__("Очки не могут быть больше 1000.")



if __name__ == '__main__':
    game_score = GameScore()
    game_score.run()


