# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1c_kFgILNVzSFj0odmmQb-vrUbG4RrH3z%26export%3Ddownload
#
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print("введите количество обрабатываемых чисел")
n = int(input())
print("введите подсчитываемую цифру")
dig = int(input())

sum_dig = 0

while n > 0:
    print("введите число")
    number = int(input())
    while number > 0:
        if number % 10 == dig:
            sum_dig += 1
        number //= 10
    n -= 1

print(f'Цифра {dig} встречалась {sum_dig} раз')
