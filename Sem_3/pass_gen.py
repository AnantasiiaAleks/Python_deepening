'''
Напишите программу, которая генерирует случайный пароль заданной длины,
состоящий из букв, цифр и специальных символов.
'''
import random
import string


pass_length = int(input('Введите длину пароля: '))
pass_chars = string.digits + string.ascii_letters + string.punctuation
password = ''.join(random.choice(pass_chars) for i in range(pass_length))

print(password)
