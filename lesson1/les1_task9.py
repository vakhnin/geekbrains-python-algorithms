# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=jhGgn7LUSzazaFBRB71W&title=lesson1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1zM8iK8lKuEx1tTLTTswxOY3cYeJBrRln%26export%3Ddownload
#
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print("Введите три числа")

a = int(input("введите первое число"))
b = int(input("введите второе число"))
c = int(input("введите третье число"))

if (a in range(b, c)) or (a in range(c, b)):
    print(f'Среднее число {a}')
elif (b in range(a, c)) or (b in range(c, a)):
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')
