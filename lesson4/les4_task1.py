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


test_prime(summa1)
test_prime(summa2)
test_prime(summa3)
