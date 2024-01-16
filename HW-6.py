import random


# 1 Задание
#
# list_num = [2, 5, 7, 8, 9, 12, 15, 19]
# first_elem = 0
# last_elem = len(list_num) - 1
#
#
# def binary_search(num: int, f_e: int, l_e: int):
#     if f_e <= l_e:
#         mid_elem = f_e + (l_e - f_e) // 2
#         if list_num[mid_elem] == num:
#             print(f"Элемент {num} находится под индексом {mid_elem}")
#         elif list_num[mid_elem] > num:
#             l_e = mid_elem - 1
#             binary_search(num, f_e, l_e)
#         else:
#             f_e = mid_elem + 1
#             binary_search(num, f_e, l_e)
#     else:
#         print(f"Элемент {num} не найден в списке {list_num}")
#
#
# binary_search(12, first_elem, last_elem)


# 2 Задание
# def to_decimal(dig: int) -> bin:
#     return bin(dig)
#
# print(to_decimal(12))

# 3 Задание
# def is_simple(dig: int) -> bool:
#     return "Число простое" if dig % 2 == 0 else "Число не простое"
#
# print(is_simple(15))

# 4 Задание

# def total_div(num_1: int, num_2: int) -> int:
#     max_value = num_1 if num_1 >= num_2 else num_2
#     nod = 0
#     i = 2
#     while i <= max_value // 2:
#         if num_1 % i == 0 and num_2 % i == 0:
#             nod = i
#             i += 1
#         else:
#             i += 1
#     if nod:
#         print(f"НОД двух чисел {num_1} и {num_2} равен {nod}" )
#     else:
#         print(f"У чисел {num_1} и {num_2} нет общего делителя")
# total_div(12, 18)
# Задание 5
# def encription_text(text: str) -> str:
#     result = ''
#     for i in text:
#        result += chr(ord(i)+3)
#     print(f"Расшифрованный текст {result}")
#
# def transcript_text(text: str) -> str:
#     result = ''
#     for i in text:
#         result += chr(ord(i) - 3)
#     print(f"Зашифрованный текст {result}")
#
#
# def input_text(user_text: str = None):
#     if not user_text:
#         user_text = input("Введите текст: ")
#     question = input("Что вы хотите сделать, зашифровать или расшифровать? ")
#     if question.lower() == 'зашифровать':
#         encription_text(user_text)
#     elif question.lower() == 'расшифровать':
#         transcript_text(user_text)
#     else:
#         print("Некоректный ввод, попробуйте еще раз")
#         input_text(user_text)
#
#
# input_text()

# Задание 7
def create_matrix(n: int, m: int):
    list_of_num = []
    for _ in range(0, n):
        temp_arr = []
        for _ in range(0, m):
            random_val = random.randint(0, 1)  # 132
            temp_arr.append(random_val)
        list_of_num.append(temp_arr)
        # print(temp_arr)
    return list_of_num


# create_matrix(10, 10)

# Задание 8
# def find_max_min_value(matrix_list):
#     max_elem = 0
#     min_elem = matrix_list[0][0]
#     idx_max = 0
#     idx_min = 0
#     max_len = len(matrix_list)
#     for list_num in matrix_list:
#         print(list_num)
#         for i in range(0, max_len):
#             if list_num[i] >= max_elem:
#                 max_elem = list_num[i]
#                 idx_max = i
#             elif list_num[i] <= min_elem:
#                 min_elem = list_num[i]
#                 idx_min = i
#     print(f"Максимальный элемент матрицы {max_elem} под индексом {idx_max} и минимальный {min_elem} с индексом {idx_min}")
#
# find_max_min_value(create_matrix(10, 10))

def to_fixed(num, dig):
    return f"{num:.{dig}f}"

# Задание 9
# def sum_matrix(matrix_list):
#     max_len = len(matrix_list)
#     sum_el = 0
#     sum_column = []
#     percent = []
#     for list in range(0, max_len):
#         column = 0
#         print(matrix_list[list])
#         for item in range(0, max_len):
#             sum_el += matrix_list[list][item]
#             column += matrix_list[item][list]
#         sum_column.append(column)
#     for i in range(0, max_len):
#         percent.append(to_fixed((sum_column[i]/sum_el*100), 2))
#     print(f"Сумма элементов столбца {sum_column}")
#     print(f"Процент от общей суммы столбца {percent}")
#     print(f"Сумма элементов матрицы {sum_el}")
#
# sum_matrix(create_matrix(10, 10))

# Задание 10

# def multyply_k(matrix_list):
#     len_list = len(matrix_list)
#     result_mlt = []
#     for i in range(0, len_list):
#         temp_arr = []
#         mlt = 0
#         k = 1
#         for j in range(0, len_list):
#             if k <= len_list - 1:
#                 mlt = matrix_list[i][j] * matrix_list[i][k]
#                 k += 1
#             else:
#                 mlt = matrix_list[i][j] * 1
#             temp_arr.append(mlt)
#         result_mlt.append(temp_arr)
#
#         print(matrix_list[i])
#         print(result_mlt[i])
#         print("------------------------------------")
#
#
# multyply_k(create_matrix(10, 10))

# Задание 11
# def multyply_l(matrix_list):
#     len_list = len(matrix_list)
#     result_mlt = []
#     k = 1
#     for i in range(0, len_list):
#         temp_arr = []
#         mlt = 0
#         for j in range(0, len_list):
#             if k <= len_list - 1:
#                 mlt = matrix_list[i][j] + matrix_list[k][j]
#             else:
#                 mlt = matrix_list[i][j]
#             temp_arr.append(mlt)
#         k += 1
#         result_mlt.append(temp_arr)
#         print(matrix_list[i])
#     print("---------------------------------------")
#     print(result_mlt)
#
#
# multyply_l(create_matrix(10, 10))

# Задание 12

# def find_elem(matrix_list, H:int):
#     max_len = len(matrix_list)
#     res_arr = []
#     for i in range(0, max_len):
#         for j in range(0, max_len):
#             if H == matrix_list[i][j]:
#                 res_arr.append(j+1)
#     print(f"Число {H} содержится в {set(res_arr)} столбце" if res_arr else f"Число {H} не содержится в матрице")
#     for i in range(0, max_len):
#         print(matrix_list[i])
# find_elem(create_matrix(10, 10), 17)

# Задание 13

# def sum_el_diag(matrix_list):
#     max_len = len(matrix_list)
#     sum_dig = []
#     sum_dig_2 = []
#     for i in range(1):
#         for j in range(0, max_len):
#             sum_dig.append(matrix_list[j][j])
#     for i in range(0, max_len):
#         k = max_len - 1 - i
#         sum_dig_2.append(matrix_list[i][k])
#         print(matrix_list[i])
#     print(f"Элементы главной диагонали {sum_dig}")
#     print(f"Сумма элементов главной диагонали {sum(sum_dig)}")
#     print(f"Элементы побочной диагонали {sum_dig_2}")
#     print(f"Сумма элементов побочной диагонали {sum(sum_dig_2)}")
# sum_el_diag(create_matrix(10, 10))


# Задание 14

# def null_matrix(matrix_list):
#     max_len = len(matrix_list)
#     for i in range(0, max_len):
#         tmp_value = 0
#         for j in range(0, max_len):
#             # if matrix_list[i][j]:
#             tmp_value += matrix_list[i][j]
#         matrix_list[i].append(tmp_value if tmp_value % 2 == 0 else tmp_value + 1)
#         print(matrix_list[i])
#
#
# null_matrix(create_matrix(10, 10))
