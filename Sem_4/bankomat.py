'''
Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляются проценты - 3%.
Нельзя снять больше, чем на счете.
При превышении суммы в 5 млн вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

def wealth_tax(balance):
    """Если баланс больше 5 млн, удержать налог 10%"""
    if balance > 5_000_000:
        tax = balance * 0.1
        balance -= tax
        print(f'Удержан налог на богатство: {tax:.2f} у.е.')
    return balance


def calc_withdrawal_fee(amount):
    """Рассчитать комиссию за снятие: 1.5%, минимум 30, максимум 600"""
    fee = amount * 0.015
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    return fee


def accrue_interest(balance):
    """Начислить 3% на текущий баланс"""
    interest = balance * 0.03
    balance += interest
    print(f'Начислены проценты: {interest:.2f} у.е.')
    return balance


def deposit(balance, amount):
    """Пополнить счет на сумму amount"""
    if amount % 50 != 0:
        print('Сумма пополнения должна быть кратна 50.')
        return balance, False
    balance += amount
    return balance, True


def withdraw(balance, amount):
    """Снять со счета сумму amount с комиссией"""
    if amount % 50 != 0:
        print('Сумма снятия должна быть кратна 50.')
        return balance, False

    fee = calc_withdrawal_fee(amount)
    total = amount + fee

    if total > balance:
        print('Недостаточно средств для снятия с учетом комиссии.')
        return balance, False

    balance -= total
    print(f"Комиссия за снятие: {fee:.2f} у.е.")
    return balance, True


def main():
    balance = 0
    operation_count = 0  # для учета операций пополнения и снятия
    history = []  # список операций (кортежи типа ("пополнение", сумма) или ("снятие", сумма))

    while True:
        balance = wealth_tax(balance)  # налог перед любой операцией

        print(f'\nТекущий баланс: {balance:.2f} у.е.')
        action = int(input('Выберите действие: 1. Пополнить  2. Снять  3. Выйти\n Введите число: '))

        if action == 3:
            print('Выход.')
            break

        elif action == 1:
            try:
                amount = int(input('Введите сумму пополнения (кратна 50): '))
            except ValueError:
                print('Некорректное значение суммы.')
                continue

            balance, success = deposit(balance, amount)
            if success:
                operation_count += 1
                history.append(('пополнение', amount))

        elif action == 2:
            try:
                amount = int(input('Введите сумму снятия (кратна 50): '))
            except ValueError:
                print('Некорректное значение суммы.')
                continue

            balance, success = withdraw(balance, amount)
            if success:
                operation_count += 1
                history.append(('снятие', amount))

        else:
            print('Неизвестное действие.')
            continue

        # Начисление 3% после каждой третьей успешной операции пополнения/снятия
        if operation_count > 0 and operation_count % 3 == 0:
            balance = accrue_interest(balance)

        print(f'Баланс после операции: {balance:.2f} у.е.')

    print('\nИстория операций:')
    for op, amt in history:
        print(f'{op.capitalize()}: {amt} у.е.')


if __name__ == '__main__':
    main()
