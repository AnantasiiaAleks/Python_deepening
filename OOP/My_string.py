'''
Создайте класс Моя Строка, где:
 будут доступны все возможности str
 дополнительно хранятся имя автора строки и
 время создания (time.time)
 Добавьте к задачам 1 и 2 строки документации для классов
'''


class My_string(str):
    """
    Модицикация класса str, в которой дополнительно
    сохраняется имя автора и дата-время создания
    """
    def __new__(cls, text, name: str):
        """
        name - имя автора
        время - из модуля datetime текущее время
        """
        import datetime
        instance = super().__new__(cls, text)
        instance.name = name
        instance.created_at = datetime.datetime.now()
        print(f'Created class {cls}, author: {instance.name}, created_at: {instance.created_at}')
        return instance




new_str = My_string('Hello world!','Anastasiia')
print(new_str.__doc__)
print(new_str.__new__.__doc__)