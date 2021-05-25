# 5. В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию в массиве.

import random

rand = [random.randint(-100, 100) for _ in range(100)]
print(f'Массив: {rand}')

min_num = 0

for i in rand:
    if rand[min_num] > i:
        min_num = rand.index(i)

if rand[min_num] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {rand[min_num]}.',
          f'Находится в массиве на позиции {min_num}')
