from _collections import deque

table = tuple("0123456789ABCDEF")

a = "A2"
b = "C4F"

if len(a) < len(b):
    a, b = b, a

print(a)
print(b)


def sum_hex(a_, b_):
    c = deque()
    transfer = 0
    while a_:
        c1 = table.index(a_.pop())
        c2 = table.index(b_.pop()) if b_ else 0
        res_spam = c1 + c2 + transfer
        if res_spam > len(table):
            res_spam -= len(table)
            transfer = 1
        else:
            transfer = 0
        c.appendleft(table[res_spam])
    if transfer:
        c.appendleft(table[transfer])
    return c


print(sum_hex(deque(a), deque(b)))
