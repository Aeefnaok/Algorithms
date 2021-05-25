# 4. Определить, какое число в массиве встречается чаще всего.

import random

rand = [random.randint(-100, 100) for _ in range(100)]
print(f'Массив: {rand}')

often = 0
for i in rand:
    if rand.count(often) < rand.count(i):
        often = rand.index(i)

print(f'Число {rand[often]}, встречается {rand.count(often)} раз(а)')
