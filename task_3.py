# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

import random

rand = [random.randint(-100, 100) for _ in range(10)]
print(f'Массив до изменения: {rand}')

max_ = rand[0]
min_ = rand[0]

for i in rand:
    if i > max_:
        max_ = i
    elif i < min_:
        min_ = i
min_num = rand.index(min_)
max_num = rand.index(max_)
rand[min_num], rand[max_num] = rand[max_num], rand[min_num]
print(f'Массив после перестановки элементов {min_num} и {max_num}: {rand}')
