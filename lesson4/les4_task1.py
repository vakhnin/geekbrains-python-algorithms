# Три реализации функции сложения чисел от 0 до n
import timeit


def test_prime(func):
    lst = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def summa1(n):
    if n == 0:
        return 0
    return n + summa1(n - 1)


def summa2(n):
    spam_sum = 0
    for i in range(n+1):
        spam_sum += i
    return spam_sum


def summa3(n):
    return n * (n + 1) // 2


# test_prime(summa1)
# test_prime(summa2)
# test_prime(summa3)

print(timeit.timeit('summa1(10)', number=100, globals=globals()))  # 0.0001571000000000003
print(timeit.timeit('summa1(20)', number=100, globals=globals()))  # 0.00041280000000000136
print(timeit.timeit('summa1(100)', number=100, globals=globals()))  # 0.0015536999999999981
print(timeit.timeit('summa1(300)', number=100, globals=globals()))  # 0.005265300000000004
print(timeit.timeit('summa1(990)', number=100, globals=globals()))  # 0.022788499999999996

print(timeit.timeit('summa2(10)', number=100, globals=globals()))  # 7.719999999999949e-05
print(timeit.timeit('summa2(20)', number=100, globals=globals()))  # 0.0001315000000000066
print(timeit.timeit('summa2(100)', number=100, globals=globals()))  # 0.0005319999999999908
print(timeit.timeit('summa2(300)', number=100, globals=globals()))  # 0.0015066999999999997
print(timeit.timeit('summa2(990)', number=100, globals=globals()))  # 0.006842899999999999

print(timeit.timeit('summa3(10)', number=100, globals=globals()))  # 2.0000000000006124e-05
print(timeit.timeit('summa3(20)', number=100, globals=globals()))  # 1.7199999999994997e-05
print(timeit.timeit('summa3(100)', number=100, globals=globals()))  # 1.8100000000007e-05
print(timeit.timeit('summa3(300)', number=100, globals=globals()))  # 2.4700000000002498e-05
print(timeit.timeit('summa3(990)', number=100, globals=globals()))  # 3.5800000000002496e-05
