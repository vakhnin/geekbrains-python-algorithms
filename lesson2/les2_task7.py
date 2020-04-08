# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1c_kFgILNVzSFj0odmmQb-vrUbG4RrH3z%26export%3Ddownload
#
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def summa(n):
    if not n > 0:
        return 0
    return n + summa(n-1)


print("введите натуральное число")
n = int(input("число:"))

res1 = summa(n)
res2 = n * (n+1) // 2

print(f'Сумма от 1 до n = {res1}')
print(f'n*(n+1)/2 = {res2}')

if res1 == res2:
    print("Результат обоих способов подсчета одинаков")
else:
    print("Что-то не так. Возможно введено не натуральное число")
