'''
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
'''

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def happy_birthday(self):
        self._age += 1
        return self._age

    def get_name(self):
        return self._name


if __name__ == '__main__':
    pers1 = Person('Mary', 4)
    print(pers1.get_name())
    print(pers1.happy_birthday())
    pers2 = Person('Mark', 6)
    print(pers2.get_name())
    print(pers2.happy_birthday())