# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
#  разработанных в рамках домашнего задания первых трех уроков.

# Решил не выбирать задание из уже усделанных ранее а выполнить задание на создание матриц

import random
import timeit
import cProfile
import sys


# №1 создание матрицы двумя циклами
def matrix_1(num_1, num_2):
    matrix = [[random.randint(1, 100) for _ in range(1, num_2)] for _ in range(1, num_1)]


print(timeit.timeit('matrix_1(10, 10)', number=1000, globals=globals()))  # 0.08452449999999999
print(timeit.timeit('matrix_1(100, 100)', number=1000, globals=globals()))  # 10.5874502

cProfile.run('matrix_1(100, 100)')


# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#   9801    0.007    0.000    0.014    0.000 random.py:200(randrange)
#   9801    0.004    0.000    0.017    0.000 random.py:244(randint)
#   9801    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.021    0.021 task_1.py:13(m_create_2_for)
#      1    0.000    0.000    0.021    0.021 task_1.py:14(<listcomp>)
#      1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#   9801    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12470    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

# --------------------------------------------------------------------------------------
# №2 Создание матрицы 1 циклом
def matrix_2(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)

    return matrix


print(timeit.timeit('matrix_2(10)', number=1000, globals=globals()))  # 0.12374689999999999
print(timeit.timeit('matrix_2(100)', number=1000, globals=globals()))  # 12.6747321

cProfile.run('matrix_2(100)')

#       62900 function calls in 0.024 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#  10000    0.007    0.000    0.014    0.000 random.py:200(randrange)
#  10000    0.004    0.000    0.017    0.000 random.py:244(randint)
#  10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.005    0.005    0.024    0.024 task_1.py:41(m_create_1_for)
#      1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#  10100    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12796    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
# ---------------------------------------------------------------------------------------------
# №3 Создание матрицы рекурсией
sys.setrecursionlimit(2000)


def matrix_rec(num_1, num_2, coll_count=0, matrix_=[]):
    matrix = []
    if coll_count + 1 == num_2:
        for _ in range(num_1):
            matrix.append(random.randint(1, 100))
        matrix_.append(matrix)
        return matrix_
    else:
        for _ in range(num_1):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        matrix_ = matrix_rec(num_1, num_2, coll_count)
        matrix_.append(matrix)
        return matrix_


print(timeit.timeit('matrix_rec(10, 10, 9)', number=1000, globals=globals()))  # 0.013299100000000008
print(timeit.timeit('matrix_rec(100, 100, 50)', number=1000, globals=globals()))  # 5.3334564

cProfile.run('matrix_rec(100, 100, 50)')

#       31508 function calls (31459 primitive calls) in 0.012 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#   5000    0.004    0.000    0.007    0.000 random.py:200(randrange)
#   5000    0.002    0.000    0.009    0.000 random.py:244(randint)
#   5000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
#   50/1    0.002    0.000    0.012    0.012 task_1.py:82(m_create_recursion)
#      1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#   5050    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#   5000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   6405    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

# Итог: сложность данного алгоритма так же О(N**2), при этом на небольшом размере матрицы (10, 10) он медленнее
# алгоритмов №1 и №2, но на размере 100 и >, он выигрывает по времени у алгоритма №2, но для таких значений требуется
# увеличение стека для рекурсии, так как при стандартном размере стек переполняется, не давая алгоритму
# выполниться.

# По итогу проведения оценки скорости работы алгоритмов можно сказать, что наиболее оптимальным
# алгоритмом для создания матриц является алгоритм №1
