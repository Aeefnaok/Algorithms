year = int(input())
print('Високосный' if not year % 400 or not year % 4 and year % 100 else 'Обычный')
