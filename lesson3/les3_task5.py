# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not len(array):
    print("Массив нулевой длины")
    exit(0)

# Немного пофантазировал в реализации алгоритма
max_index = None

for i in range(len(array)):
    if max_index is None:
        if array[i] < 0:
            max_index = i
    elif 0 > array[i] > array[max_index]:
        max_index = i

print("Исходный массив")
print(array)

if max_index is None:
    print("В массиве нет отрицательных элементов")
else:
    print(f'Максимальный отрицательный элемент: {array[max_index]} в позиции: {max_index}')
