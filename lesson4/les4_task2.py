# Простое n число


def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(lst, start=1):
        assert item == func(i)
        print(f'Test {i} OK')


def sieve(n):
    sieve_arr = [i for i in range(n*n+2)]   # квадратные скобки только для этой задачи, а не для ПЗ 2
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


test_prime(sieve)
