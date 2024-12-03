'''
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
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

class Employee(Person):
    PASS_VALUE = 7
    MIN_ID = 100_000
    MAX_ID = 999_999
    
    def __init__(self, user_id, name, age):
        super().__init__(name, age)
        if user_id < self.MIN_ID or user_id > self.MAX_ID:
            self.user_id = self.MIN_ID
        else:
            self.user_id = user_id

    def get_access(self):
        user_id_str = str(self.user_id)
        s = sum(int(num) for num in user_id_str)
        return s % self.MAX_ID


    
    
if __name__ == '__main__':
    emp = Employee(345673, 'Kirill', 36)
    #print(id(emp))
    #print(emp.get_name())
    print(emp.get_access())
    
    