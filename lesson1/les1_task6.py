# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=jhGgn7LUSzazaFBRB71W&title=lesson1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1zM8iK8lKuEx1tTLTTswxOY3cYeJBrRln%26export%3Ddownload
#
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print("Введите номер буквы:")
n = int(input())

if n in range(1, 27):
    res = chr(ord("a") + n - 1)
    print(f'Буква с данным номером это {res}')
else:
    print("Номер буквы не входит в диапазон возможных букв")
