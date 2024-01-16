import random
import math
import sympy

# 2 Задание

N = 1470
k = 0
flag_sunday = 0
days = 0
qnty_sunday = 0
while k <= N:
    if flag_sunday <= 6:
        k += 20
        flag_sunday += 1
        days += 1
    else:
        days += 1
        qnty_sunday += 1
        flag_sunday = 0
print(f"Маша накопит на телефон за {days} дня из которых {qnty_sunday} воскресений")

# 3 Задание

list_fib_number = []
prev_value = 0
next_value = 1
for i in range(1, 16):
    fib_num = prev_value + next_value
    prev_value, next_value = next_value, fib_num
    list_fib_number.append(fib_num)

print(list_fib_number)

# 4 Задание

list_of_number = []
for _ in range(1, 15):
    list_of_number.append(random.randint(1, 99))
print(f"Список случайных элементов: {list_of_number}")
sum = 0
max_value = 0
min_value = list_of_number[0]
for i in range(0, len(list_of_number)):
    sum += list_of_number[i]
    if max_value < list_of_number[i]:
        max_value = list_of_number[i]
    elif min_value > list_of_number[i]:
        min_value = list_of_number[i]
print(f"Сумма элементов списка: {sum}")
print(f"Мвксимальное значение списка: {max_value}")
print(f"Минимальное значение списка: {min_value}")

# 5 Задание

list_of_number = []
for _ in range(1, 15):
    list_of_number.append(random.randint(1, 99))
print(f"Список элементов: {list_of_number}")

N = len(list_of_number)
same_number_list = []
cnt = 0
for i in range(0, N - 1):
    top = i
    for j in range(top + 1, N):
        if list_of_number[j] == list_of_number[i]:
            same_number_list.append(list_of_number[i])
if (same_number_list):
    print(f"Список повторяющихся значений {same_number_list}")
    for i in range(0, len(same_number_list)):
        cnt = list_of_number.count(same_number_list[i])
        print(f"Число {same_number_list[i]} повторяется {cnt} раз(а)")
    quit()
print("Все элементы уникальны")

# 6 Задание
list_of_num = [2, 3, 5, 6, 9, 13, 21, 32]
search_num = 21

firs_element = 0
last_element = len(list_of_num) - 1
while firs_element <= last_element:
    middle = firs_element + (last_element - firs_element) // 2
    if list_of_num[middle] == search_num:
        print(f"Элемент находится под индексом: {middle}")
        quit()
    elif list_of_num[middle] < search_num:
        firs_element = middle + 1
    else:
        last_element = middle - 1
print(f"Элемент {search_num} не найден в списке {list_of_num}")

# 7 Задание
list_of_num = [5, 6, 7, 1, 2, 3, 4]
search_num = 5

firs_element = 0
last_element = len(list_of_num) - 1
while firs_element <= last_element:
    mid_elem = firs_element + (last_element - firs_element) // 2
    if list_of_num[mid_elem] == search_num:
        print(f"Элемент находится под индексом: {mid_elem}")
        quit()
    elif list_of_num[mid_elem] >= list_of_num[firs_element]:
        if list_of_num[mid_elem] >= search_num >= list_of_num[firs_element]:
            last_element = mid_elem - 1
        else:
            firs_element = mid_elem + 1
    else:
        if list_of_num[mid_elem] <= search_num <= list_of_num[last_element]:
            firs_element = mid_elem + 1
        else:
            last_element = mid_elem - 1
print(f"Элемент {search_num} не найден в списке {list_of_num}")

# 1 задание

x = 14
result = 0.0
n = 100

for i in range(0, n + 1):
    result += (-1) ** i * x ** (2 * n) / math.factorial(2 * n)
print(f"cos(x) = {math.cos(x)}")
print(f"Сумма элементов : {result}")
