'''
Напишите программу, которая принимает строку и определяет, является ли она
палиндромом (читается одинаково с обеих сторон).
'''
string = input("Введите текст: ").lower().replace(' ', '')

odd_chars = set()

for char in string:
    if char in odd_chars:
        odd_chars.remove(char)
    else:
        odd_chars.add(char)
if len(odd_chars) <= 1:
   print("Строка является палиндромом")
else:
   print("Строка не является палиндромом")