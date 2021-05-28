# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».

import math
import timeit
import cProfile


def sieve_without_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
    '''

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена»
    '''

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print(sieve_without_eratosthenes(user_number))

print('Алгоритм 1 без использования алгоритма «Решето Эратосфена»')
print(
    f'{sieve_without_eratosthenes(user_number)} - {user_number} \
по счёту простое число'
)

print('Алгоритм 2 с использованием алгоритма «Решето Эратосфена»')
print(
    f'{sieve_eratosthenes(user_number)} - {user_number} по счёту простое число')

# print(timeit.timeit('sieve_without_eratosthenes(100)', number=1000, globals=globals()))  # 0.7230837999999999

# cProfile.run('sieve_without_eratosthenes(100)')
#       1182 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 task_2.py:11(sieve_without_eratosthenes)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    539    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# print(timeit.timeit('sieve_eratosthenes(100)', number=1000, globals=globals()))  #12.3186172

# cProfile.run('sieve_eratosthenes(100)')

#       1418 function calls in 0.012 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#      1    0.010    0.010    0.011    0.011 task_2.py:30(sieve_eratosthenes)
#      1    0.000    0.000    0.000    0.000 task_2.py:36(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_2.py:48(prime_counting_function)
#      1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#    118    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    647    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    118    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#    529    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
