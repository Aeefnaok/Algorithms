# Решение с помощью массива:

import sys

n = int(input('Введите число:'))

memory = sys.getsizeof(n)

a = []

while n > 0:
    a.append(n % 10)
    n = n // 10

memory = memory + sys.getsizeof(a) + sys.getsizeof(''.join(map(str, a)))

print('Обратное число:', ''.join(map(str, a)))
print("В программе задействовано байт памяти:", memory)

# Возьмем число 123456789
# Обратное число:  987654321
# В программе задействовано байт памяти: 270 на переменную, массив и строку

# Возьмем число 1234567890987654321234567890987654321
# Обратное число:  1234567890987654321234567890987654321
# В программе задействовано байт памяти: 550
