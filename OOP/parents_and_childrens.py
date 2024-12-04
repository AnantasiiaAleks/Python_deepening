'''
 Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
 Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
 ● имя,
 ● возраст,
 ● список детей.
 И он может:
 ● сообщить информацию о себе,
 ● успокоить ребёнка,
 ● покормить ребёнка.
 У ребёнка есть:
 ● имя,
 ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
 ● состояние спокойствия,
 ● состояние голода.
 Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
 и словарь состояний, и что-то поинтереснее.
'''



class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def say_self_info(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.')

    def add_child(self, child):
        if self.age - child.age > 16:
            self.children.append(child)
            print(f'Ребенок {child} добавлен в семью {self.name}.')
        else:
            print(f'Ребенок {child} слишком взрослый.')

    def feed(self, child):
        if child in self.children:
            child.hungry = False
            print(f'Ребенок {child} накормлен.')
        else:
            print(f'Ребенок {child} не в семье.')

    def calm(self, child):
        if child in self.children:
            child.angry = False
            print(f'Ребенок {child} успокоен.')
        else:
            print(f'Ребенок {child} не в семье.')

    def say_about_children(self):
        if self.children:
            print(f'У {self.name} есть дети:')
            for num, child in enumerate(self.children):
                print(f'{num} - {child}')

class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.angry = True
        self.hungry = True

    def say_self_info(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.')

    def say_self_status(self):
        angry_status = 'Зол' if self.angry else 'Спокоен'
        hungry_status = 'Голоден' if self.hungry else 'Сыт'
        print(f'Ребенок {self.name} {angry_status} и {hungry_status}')

    def __str__(self):
        return f'Ребенок {self.name}, {self.age} лет.'



if __name__ == '__main__':
    parent = Parent("Иван", 40)
    child1 = Child("Анна", 27)
    child2 = Child("Петя", 10)
    child3 = Child("Маша", 3)

    for child in [child1, child2, child3]:
        parent.add_child(child)
    # Выводинформацииородителеиегодетях
    parent.say_self_info()
    parent.say_about_children()
    for child in parent.children:
        parent.feed(child)
        parent.calm(child)
        child.say_self_status()