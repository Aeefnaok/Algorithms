# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят и сколько между ними находится букв.

letter_1, letter_2 = [
  x.upper() for x in input('Введите две буквы, через пробел (A - Z): ').split()
]

# Генерация списка букв
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter_1 = abc_list.index(letter_1) + 1
index_letter_2 = abc_list.index(letter_2) + 1

if index_letter_1 < index_letter_2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter_1}, находится на позиции: {index_letter_1}')
print(f'Вторая буква {letter_2}, находится на позиции: {index_letter_2}')

print(
    f'Между ними находятся буквы \
{abc_list[abc_list.index(letter_1) + step:abc_list.index(letter_2):step]} \
({abs(index_letter_1 - index_letter_2) - 1})'
        )
