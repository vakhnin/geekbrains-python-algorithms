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
