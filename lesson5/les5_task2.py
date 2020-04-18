from _collections import deque

table = tuple("0123456789ABCDEF")

a = deque("A2")
b = deque("C4F")
c = deque()

if len(a) < len(b):
    a, b = b, a

print(a)
print(b)


def sum_hex(a, b):
    transfer = 0
    while a:
        c1 = table.index(a.pop())
        c2 = table.index(b.pop()) if b else 0
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


print(sum_hex(a, b))
