# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
from timeit import timeit

MAX_SIZE = 10
NUMBER_EXECUTIONS = 10_000


def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        flag = True
        for n in range(i):
            if data[n] > data[n+1]:
                data[n], data[n+1] = data[n+1], data[n]
                flag = False

        if flag == True:
            break
    return data


def bubble_sort_slow(data):
    for i in range(len(data) - 1, 0, -1):
        for n in range(i):
            if data[n] > data[n+1]:
                data[n], data[n+1] = data[n+1], data[n]

    return data


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
              setup='from __main__ import bubble_sort',
              number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_slow({numbers})',
              setup='from __main__ import bubble_sort_slow',
              number=NUMBER_EXECUTIONS)
print(time1)
print(time2)
