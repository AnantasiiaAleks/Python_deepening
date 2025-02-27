'''
Треугольник существует только тогда, когда сумма любых двух его сторон
больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
хотя бы в одном случае отрезок окажется больше суммы двух других, то
треугольника с такими сторонами не существует. Отдельно сообщить является
ли треугольник разносторонним, равнобедренным или равносторонним.
'''

a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника не существует')
else:
    if a == b or a == c or b == c:
        print('Треугольник равносторонний')
    elif a == b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')