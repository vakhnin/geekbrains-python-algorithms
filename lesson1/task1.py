# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

sumDigs = 0
multDigs = 1
n = int(input("Введите целое число из 3 цифр:"))

sumDigs += n % 10
multDigs *= n % 10
n = n // 10

sumDigs += n % 10
multDigs *= n % 10
n = n // 10

sumDigs += n % 10
multDigs *= n % 10

print(f'Сумма цифр: {sumDigs}')
print(f'Произведение цифр: {multDigs}')
