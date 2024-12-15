'''
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
�
� При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков
архивов
 📌 list-архивы также являются свойствами экземпляра
 Добавьте к задачам 1 и 2 строки документации для классов
'''

class Archive:
    """
    Класс архив, сохраняющий при каждом последующем
    создании экземпляра данные из прошлых экземпляров
    в отдельные списки
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums = []
            cls._instance.strings = []
        else:
            cls._instance.nums.append(cls._instance.num)
            cls._instance.strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string

    def __str__(self):
        return f'Экземпляр класса Archive со свойствами: {self.num}, {self.string}'

    def __repr__(self):
        return f"Archive({self.num}, '{self.string}')"

archive1 = Archive(3, 'string1')
archive2 = Archive(5, 'string2')
archive3 = Archive(8, 'string3')
archive4 = Archive(8, 'string3')

print(archive3.nums)
print(archive3.strings)
print(archive2.__doc__)
print(archive1)
print(archive4.strings)
print(f'{archive1=}')