 ## Задание 1. Карма
 Один буддист-программист решил создать свой симулятор жизни, в котором
 нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
 
Каждый день вызывается специальная функция one_day(), которая возвращает
 количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
 исключений:
- KillError,
- DrunkError,
- CarCrashError,
- GluttonyError,
- DepressionError.
 
(Исключения нужно создать самостоятельно, при помощи наследования от
 Exception.)

Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
 которого возможен только при накоплении кармы до уровня константы.
 Исключения обработайте и запишите в отдельный лог karma.log.

По итогу у вас может быть примерно такая структура программы:
- открываем файл
- цикл по набору кармы
- try
- карма += one_day()
- except(ы) с указанием классов исключений, которые нужно поймать
- добавляем запись в файл
- закрываем файл
 
### Подсказка №1
Создайте пользовательские исключения с помощью на следования от Exception.
Создайте классы для каждого типа исключения, унаследовав их от базового класса
 Exception, и определите их сообщения в конструкторе.

### Подсказка №2
Используйте модуль random для генерации случайных чисел. Модуль random поможет
 вам как для генерации случайных чисел для кармы, так и для случайного выбора
 исключений.

### Подсказка №3
Обработайте исключения внутри блока try-except и запишите их в файл. Используйте
 конструкцию try-except для перехвата исключений и записи их сообщений в файл
 karma.log.

### Подсказка №4
Откройте файл в режиме записи с помощью with для автоматического управления
 ресурсами. Использование конструкции with open(...) обеспечит автоматическое
 закрытие файла после завершения работы с ним.