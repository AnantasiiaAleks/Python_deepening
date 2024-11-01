'''
✔ Напишите программу, которая выводит на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
'''
LOW_LIMIT = 1
UP_LIMIT = 100
DIV_1 = 3
DIV_2 = 5


for num in range(LOW_LIMIT, UP_LIMIT + 1):
    if num % (DIV_1 * DIV_2) == 0:
        print('FizzBuzz')
    elif num % DIV_1 == 0:
        print('Fizz')
    elif num % DIV_2 == 0:
        print('Buzz')
    else:
        print(num)

print(*(
    'FizzBuzz' if num % (DIV_1 * DIV_2) == 0 \
    else 'Fizz' if num % DIV_1 == 0 \
    else 'Buzz' if num % DIV_2 == 0 \
    else num \
    for num in range(LOW_LIMIT, UP_LIMIT + 1)
), sep=', ')