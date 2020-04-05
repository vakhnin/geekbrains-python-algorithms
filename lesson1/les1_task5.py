# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=jhGgn7LUSzazaFBRB71W&title=lesson1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1zM8iK8lKuEx1tTLTTswxOY3cYeJBrRln%26export%3Ddownload
#
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print("Введите две буквы")
l1 = input("введите первую букву: ")
l2 = input("введите вторую букву: ")

pos_l1 = ord(l1) - ord("a") + 1
pos_l2 = ord(l2) - ord("a") + 1

print(f'Позиция первой буквы: {pos_l1}')
print(f'Позиция второй буквы: {pos_l2}')

diff_pos = abs(pos_l1 - pos_l2)
if diff_pos > 0:
    diff_pos -= 1

print(f'Между буквами {diff_pos} букв')
