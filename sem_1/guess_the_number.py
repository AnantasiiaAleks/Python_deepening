'''
Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов
мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать
число за семь попыток.
'''
min_value = 1
max_value = 100

count = 1

while True:
    n = (min_value + max_value) // 2
    print(f'Попытка № {count}')
    print(f'Твоё число равно, меньше или больше, чем число {n}?')
    answer = int(input('1 — равно, 2 — больше, 3 — меньше: '))
    match answer:
        case 1:
            print('Победа!')
            break
        case 2:
            min_value = n
            count += 1
        case 3:
            max_value = n
            count += 1