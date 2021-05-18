# 1. Найти сумму и произведение цифр трехзначного числа,
#   которое вводит пользователь.
# https://drive.google.com/file/d/12bOq2NRP2JbBZN8eEmV1qrrGcU3QNQRg/view?usp=sharing
num = int(input("Введите трехзначное число: "))

num_1 = num % 10
num_2 = num % 100 // 10
num_3 = num // 100
summ = num_1 + num_2 + num_3
prod = num_1 * num_2 * num_3
print(f"Сумма цифр введенного числа: {summ}")
print(f"Произведение цифр введенного числа: {prod}")
