import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100 - 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def test_sort(arr):
    for i in range(len(arr)-1):
        assert arr[i] >= arr[i+1]
    print('Массив отсортирован по убыванию')


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1


print("Исходный массив")
print(array)
bubble_sort(array)
test_sort(array)
print('Массив после сортировки')
print(array)
