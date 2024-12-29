import os
from random import randint


LUCKY_SUM = 777


class Lucky_number:
    def __init__(self,filename):
        """Инициализация с именем файла и определение пути к файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return os.path.join(os.path.abspath('.'),self.filename)

    def for_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать ошибку."""
        return randint(1,13) == 4

    def del_file(self):
        """Удаляет файл, если он существует."""
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')

    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в файл."""
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.for_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path,'a') as out_fd:
                out_fd.write(str(input_number)+'\n')
        except(ValueError,KeyboardInterrupt)as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.del_file()             # Удаляет старый файл, если он существует
        while self.magic_sum < LUCKY_SUM:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')



if __name__ == "__main__":
    program = Lucky_number('out_file.txt')
    program.run()