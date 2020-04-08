# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson2.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1c_kFgILNVzSFj0odmmQb-vrUbG4RrH3z%26export%3Ddownload
#
#  Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, надо вывести 6843

print("введите натуральное число")
n = int(input("число:"))

rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print(f'обратное число: {rev}')
