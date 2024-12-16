class Stack:
    """
    Класс Стек, реализующий принцип LIFO
    """
    def __init__(self):
        self.__stack = list()

    def pop(self):
        """Извлечение элемента, если стек не пустой"""
        if self.is_empty():
            return None
        return self.__stack.pop()

    def push(self, item):
        """Добавление элемента"""
        self.__stack.append(item)

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.__stack) == 0

    def get_top(self):
        """Получение последнего элемента стека без его удаления"""
        if self.is_empty():
            return None
        return self.__stack[-1]


class TaskManager:
    """Класс, реализующий возможности стека"""

    def __init__(self):
        self.tasks = dict()

    def new_task(self, priority: int, text: str) -> None:
        """
        Добавление новой задачи в словарь: ключ - priority, значение - text
        :param priority: приоритет задачи (чем меньше число, тем выше приоритет)
        :param text: - текст задачи
        """
        if priority not in self.tasks.keys():
            self.tasks[priority] = Stack()
        self.tasks[priority].push(text)


    def remove_task(self, text: str) -> None:
        """
        Удаление задачи по значению из всех стеков
        :param text: текст задачи
        """
        for stack in self.tasks.values():
            temp_stack = Stack()
            while not stack.is_empty():
                task = stack.pop()
                if task != text:
                    temp_stack.push(task)
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())

    def __str__(self):
        sorted_keys = sorted(self.tasks.keys())
        output = []
        for key in sorted_keys:
            task_line = [str(key)]
            temp_stack = Stack()
            while not self.tasks[key].is_empty():
                task = self.tasks[key].pop()
                temp_stack.push(task)
            while not temp_stack.is_empty():
                task_line.append(temp_stack.pop())

            output.append(' * '.join(task_line))
        return '\n'.join(output)


def program():
    taskmanager = TaskManager()
    taskmanager.new_task(4, 'Убраться')
    taskmanager.new_task(4, 'Вымыть посуду')
    taskmanager.new_task(1, 'Поспать')
    taskmanager.new_task(2, 'Погулять')
    taskmanager.new_task(2,'Приготовить поесть')

    print(taskmanager)



if __name__ == '__main__':
    program()