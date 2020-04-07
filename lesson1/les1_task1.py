# Ссылка на блок-схему (страницы листаются):
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=jhGgn7LUSzazaFBRB71W&title=lesson1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1zM8iK8lKuEx1tTLTTswxOY3cYeJBrRln%26export%3Ddownload
#
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print("Введите целое число из 3 цифр:")
n = int(input())

sumDigs = n % 10
multDigs = n % 10
n = n // 10

sumDigs += n % 10
multDigs *= n % 10
n = n // 10

sumDigs += n % 10
multDigs *= n % 10

print(f'Сумма цифр: {sumDigs}')
print(f'Произведение цифр: {multDigs}')
