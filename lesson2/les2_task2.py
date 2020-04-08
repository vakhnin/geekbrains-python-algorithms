# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1c_kFgILNVzSFj0odmmQb-vrUbG4RrH3z%26export%3Ddownload
#
#  Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print("введите натуральное число")
n = int(input("число:"))

odd = 0
even = 0

while n > 0:
    if n % 10 % 2:
        odd += 1
    else:
        even += 1
    n = n // 10

print(f'четных цифр {even}')
print(f'нечетных цифр {odd}')
