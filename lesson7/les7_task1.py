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
    is_swap = True
    idx_swap = len(arr) - 1
    # Если на предыдущем проходе не менялись местами элементами, массив отсортирован, выходим
    while is_swap:
        is_swap = False
        # После элементов обмена массив можно не проходить. Хвост массива уже отсортирован
        for i in range(idx_swap):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                idx_swap = i
                is_swap = True


print("Исходный массив")
print(array)
bubble_sort(array)
test_sort(array)
print('Массив после сортировки')
print(array)
