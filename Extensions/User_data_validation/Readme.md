## Задача 5. Валидатор Пользовательских Данных

Создайте класс User, который содержит атрибуты name, email, и age.

Необходимо убедиться, что:
- Имя состоит из хотя бы двух слов, каждое из которых начинается с заглавной буквы.
- Электронная почта содержит символ @ и точку. после @.
- Возраст — это положительное целое число, не меньше 0 и не больше 120.

Создайте пользовательские исключения для каждой из этих проверок:
- NameError:Если имя не соответствует формату.
- EmailError: Если электронная почта не соответствует формату.
- AgeError: Если возраст вне допустимого диапазона.
 
### Подсказка №1
Создайте пользовательские исключения.
Определите три класса исключений (NameError, EmailError, AgeError), наследующие от базового класса Exception.
Установите сообщения об ошибках в конструкторах этих классов, чтобы указать, какие именно ошибки произошли.
### Подсказка №2
Используйте свойства (геттеры и сеттеры) в классе User для контроля установки значений атрибутов 
name, email, и age. Это позволяет выполнять проверки перед присваиванием значений.
### Подсказка №3
Убедитесь, что имя состоит из хотя бы двух слов, каждое из которых начинается с заглавной буквы.
Используйте метод split() для разделения имени на слова и проверьте первый символ каждого слова с помощью isupper().
### Подсказка №4
Убедитесь, что электронная почта содержит символ @ и точку . после символа @.
Используйте метод split('@') для разделения строки и проверяйте наличие точки в части после @.
### Подсказка №5
Убедитесь, что возраст является целым числом в пределах от 0 до 120.
Используйте функцию isinstance() для проверки типа данных и операторы сравнения для проверки диапазона.