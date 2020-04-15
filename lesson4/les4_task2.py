# Простое n число
import timeit
import cProfile
from math import sqrt


def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(lst, start=1):
        assert item == func(i)
        print(f'Test {i} OK')


def sieve(n):
    sieve_arr = [i for i in range(n * n + 2)]  # квадратные скобки только для этой задачи, а не для ПЗ 2
    sieve_arr[1] = 0
    len_sieve_arr = len(sieve_arr)
    for i in range(2, len_sieve_arr):
        if sieve_arr[i] != 0:
            j = i + i
            while j < len_sieve_arr:
                sieve_arr[j] = 0
                j += i

    for i in sieve_arr:
        if i != 0:
            if n > 1:
                n -= 1
            else:
                return i


def prime(n):
    prime_arr = [2, 3, 5, 7]
    for i in range(11, n * n + 2, 2):
        if len(prime_arr) >= n:
            break
        if (i % 2 == 0) or (i % 10 == 5):
            continue
        for j in prime_arr:
            if j > sqrt(i):
                prime_arr.append(i)
                break
            if i % j == 0:
                break
    return prime_arr[n-1]


# test_prime(sieve)

# print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.0024107000000000017
# print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.0841172
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.3424142
# print(timeit.timeit('sieve(300)', number=100, globals=globals()))  # 3.5862416999999995
# print(timeit.timeit('sieve(500)', number=100, globals=globals()))  # 11.060683000000001

# cProfile.run('sieve(10)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:14(<listcomp>)
# cProfile.run('sieve(50)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:14(<listcomp>)
# cProfile.run('sieve(100)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:14(<listcomp>)
# cProfile.run('sieve(300)')  # 1    0.003    0.003    0.003    0.003 les4_task2.py:14(<listcomp>)
# cProfile.run('sieve(500)')  # 1    0.009    0.009    0.009    0.009 les4_task2.py:14(<listcomp>)

test_prime(prime)
