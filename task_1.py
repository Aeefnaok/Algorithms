# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.



import collections
import random


def sum_tuple(numbers):
    '''tuple --> sum'''

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Company = collections.namedtuple('Company', ['q1', 'q2', 'q3', 'q4'])

base_company = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_company[name] = Company(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

base_company['Name1'] = Company(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

base_company['Name2'] = Company(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

total_profit = ()

for name, profit in base_company.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_company)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_company.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in base_company.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')
