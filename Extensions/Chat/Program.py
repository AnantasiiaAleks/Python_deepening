class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename


    def display_messages(self):
        """Отображает все сообщения из файла."""
        try:
            with open(self.filename, 'r', encoding='UTF-8') as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: сообщений не найдено\n")


    def add_message(self, name, message):
        """Добавляет новое сообщение в файл."""
        with open(self.filename, 'a', encoding='UTF-8') as file:
            file.write(f"{name}: {message}\n")


    def run(self):
        """Запускает основной цикл чата."""
        name = input("Введите ваше имя: ")
        while True:
            print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2, для выхода введите 0")
            answer = input("Введите 1 или 2: ")
            if answer == '1':
                self.display_messages()
            elif answer == '2':
                new_message = input("Введите сообщение: ")
                self.add_message(name, new_message)
            elif answer == '0':
                exit()
            else:
                print("Неизвестная команда\n")




if __name__ == "__main__":
    chat = Chat()
    chat.run()