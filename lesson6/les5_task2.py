from collections import deque
import random

TABLE = tuple("0123456789ABCDEF")
SIZE = len(TABLE)
INDEX = {}
print(iter(TABLE))
for j, item in enumerate(TABLE):
    INDEX[item] = j


def sum_hex(n1, n2):
    a_ = n1
    b_ = n2

    result = deque()
    overflow = 0

    if len(a_) < len(b_):
        a_, b_ = b_, a_

    while a_:
        d1 = INDEX[a_.pop()]
        d2 = INDEX[b_.pop()] if b_ else 0
        res_spam = d1 + d2 + overflow
        if res_spam >= SIZE:
            res_spam -= SIZE
            overflow = 1
        else:
            overflow = 0
        result.appendleft(TABLE[res_spam])
    if overflow:
        result.appendleft(TABLE[overflow])
    return result


def mult_hex(n1, n2):
    a_ = n1
    b_ = n2

    result = deque('0')
    shift = 0

    while b_:
        d2 = INDEX[b_.pop()]
        c_part = deque()
        overflow = 0
        for i in range(len(a_)-1, -1, -1):
            spam = INDEX[a_[i]] * d2 + overflow
            c_part.appendleft(TABLE[spam % SIZE])
            overflow = spam // SIZE
        if overflow:
            c_part.appendleft(TABLE[overflow])

        for i in range(shift):
            c_part.append('0')
        shift += 1
        result = sum_hex(result, c_part)

    return result


def test_sum(func):
    for i in range(15):
        a_ = random.randint(0, 5000)
        b_ = random.randint(0, 5000)
        assert f'{a_ + b_:X}' == ''.join(func(deque(f'{a_:X}'), deque(f'{b_:X}')))
        print(f'Test {a_:X}+{b_:X}={a_ + b_:X} OK')


def test_mult(func):
    for i in range(15):
        a_ = random.randint(0, 5000)
        b_ = random.randint(0, 5000)
        assert f'{a_ * b_:X}' == ''.join(func(deque(f'{a_:X}'), deque(f'{b_:X}')))
        print(f'Test {a_:X}*{b_:X}={a_ + b_:X} OK')


# a = input('Введите первое число:').upper()
# b = input('Введите второе число:').upper()

a = "A2"
b = "C4F"

# test_sum(sum_hex)
test_mult(mult_hex)

print(''.join(sum_hex(deque(a), deque(b))))
print(''.join(mult_hex(deque(a), deque(b))))
