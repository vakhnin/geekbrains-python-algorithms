# В этом задании использована коллекция dictionary
QUARTERS = 4
companies = {}

n = int(input('Введите количество преприятий:'))
sum_profit = 0
for i in range(n):
    year_profit = 0
    spam_profit = []
    print()
    name_company = input(f'Введите название {i+1}-го предприятия:')
    for j in range(QUARTERS):
        spam_profit.append(int(input(f'Введите прибыль предприятия "{name_company}" за {j+1}-й квартал:')))
    sum_profit += sum(spam_profit)
    companies[name_company] = spam_profit

print(f'Средняя прибыль за год {sum_profit / n:.2f}')
print('Предприятия с прибылью за год больше средней:')
for i in companies:
    if sum(companies[i]) > sum_profit / n:
        print(i)
print('Предприятия с прибылью за год меньше или равной средней:')
for i in companies:
    if sum(companies[i]) <= sum_profit / n:
        print(i)
