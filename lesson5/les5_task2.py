# В этом задании использована коллекция deque
from collections import deque
import random

TABLE = tuple("0123456789ABCDEF")


def sum_hex(a_, b_):
    c = deque()
    transfer = 0

    if len(a_) < len(b_):
        a_, b_ = b_, a_

    while a_:
        c1 = TABLE.index(a_.pop())
        c2 = TABLE.index(b_.pop()) if b_ else 0
        res_spam = c1 + c2 + transfer
        if res_spam >= len(TABLE):
            res_spam -= len(TABLE)
            transfer = 1
        else:
            transfer = 0
        c.appendleft(TABLE[res_spam])
    if transfer:
        c.appendleft(TABLE[transfer])
    return c


def test_sum(func):
    for i in range(15):
        a_ = random.randint(0, 5000)
        b_ = random.randint(0, 5000)
        assert f'{a_+b_:X}' == ''.join(func(deque(f'{a_:X}'), deque(f'{b_:X}')))
        print(f'Test {a_:X}+{b_:X}={a_+b_:X} OK')


a = input('Введите первое число:')
b = input('Введите второе число:')

test_sum(sum_hex)

print(''.join(sum_hex(deque(a), deque(b))))
