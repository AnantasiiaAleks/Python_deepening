'''
 Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
'''


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_are_you(self):
        return type(self)

class Fish(Animal):
    def __init__(self, swim, name, age):
        super().__init__(name, age)
        self.swim = swim

    def can_swim(self):
        return f'I can swim!'

class Bird(Animal):
    def __init__(self, fly, name, age):
        super().__init__(name, age)
        self.fly = fly

    def can_fly(self):
        return f'I can fly!'

class Cat(Animal):
    def __init__(self, myau, name, age):
        super().__init__(name, age)
        self.myau = myau

    def say_myau(self):
        return f'I say "Purrr"!'


if __name__ == '__main__':
    fish = Fish('swim', 'Byanka', 3)
    print(fish.who_are_you(), fish.can_swim())
    bird = Bird('fly', 'Chayka', 2)
    print(bird.who_are_you(), bird.can_fly())
    cat = Cat('Myau', 'Vaska', 5)
    print(cat.who_are_you(), cat.say_myau())