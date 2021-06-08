#  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
#  в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).


from random import randint as rand

m = 3

data = [rand(0, 100) for el in range(2 * m + 1)]


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i], data[i - 1] = data[i - 1], data[i]
            if i > 1:
                i -= 1
    return data


def nlogn_median(data):
    data = gnome(data)
    if len(data) % 2 == 1:
        return data[len(data) // 2]
    else:
        return 0.5 * (data[len(data) // 2 - 1] + data[len(data) // 2])


print(f'{data} исходный массив \n{gnome(data)} отсортированный массив')
print(nlogn_median(data), "- медиана данного массива")
