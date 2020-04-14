# Простое n число

n = 2100
sieve = [i for i in range(n)]   # квадратные скобки только для этой задачи, а не для ПЗ 2
sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i

print(sieve)
res = [i for i in sieve if i != 0]
print(res)
