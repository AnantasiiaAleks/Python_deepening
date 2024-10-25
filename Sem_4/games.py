'''
Правила игры «Камень, ножницы, бумага»: программа запрашивает у
пользователя строку и выводит, победил он или проиграл. Камень бьёт
ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число
до тех пор, пока он не отгадает загаданное.
'''
from random import randint


def rock_paper_scissors():
    """ Здесь будет игра «Камень, ножницы, бумага»"""

    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: "))
    computer = randint(1, 3)

    if player == computer:
        print('Ничья!')
        mainMenu()
    elif (player == 1 and computer == 2)\
            or (player == 2 and computer == 3)\
            or (player == 3 and computer == 1):
        print('Вы выиграли!')
        mainMenu()
    elif (computer == 1 and player == 2)\
            or (computer == 2 and player == 3)\
            or (computer == 3 and player == 1):
        print('Вы проиграли!')
        mainMenu()
    else:
        print('Неверный ввод')
        mainMenu()


def guess_the_number():
    """ Здесь будет игра «Угадай число»"""
    computer = randint(1, 10)
    flag = True
    while flag:
        player = int(input('Загадано число от 1 до 10. Ваши предположения: '))
        if player == computer:
            print('Вы угадали!')
            mainMenu()
        elif player > computer:
            print('Слишком много!')
        elif player < computer:
            print('Слишком мало!')
        else:
            print('Неверный ввод.')
            mainMenu()


def mainMenu():
    """Здесь главное меню игры"""
    print('Добро пожаловать!\n'
          'Выберите игру:\n'
          '1 - Камень-ножницы-бумага\n'
          '2 - Угадай число\n'
          '0 - Выход из программы')

    choice = int(input('Чего изволите: '))

    match choice:
        case 0:
            print('Bye-bye!')
            exit()
        case 1:
            rock_paper_scissors()
        case 2:
            guess_the_number()


mainMenu()
