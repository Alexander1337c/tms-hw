import random
import time

# # 1 Задание


# list_num = [0, 1, 2, 3]
# print(f"1-е задание {list(map(lambda x: str(x), list_num))}")
#
# # 2 Задание
#
# print(f"2-е задание {list(filter(lambda item: item > 0, list_num))}")
#
# # 3 задание
# list_of_world = ['asddsa', 'dsareq', 'abccba', 'gjfjere']
# print(f"3-е заданеие {list(filter(lambda item: item == item[::-1], list_of_world))}")
#
#
# # 4 задание
#
# def select(fn_1):
#     def inner(*args):
#         start_time = time.time()
#         fn_1(*args)
#         end = time.time()
#         print(f"Затраченное время на выполнение декоратора {(end - start_time):.2f}")
#
#     return inner
#
#
# list_num = list([random.randint(0, 100) for x in range(0, 1000000)])
#
#
# @select
# def spent_time(list_num):
#     return list(map(lambda x: x ** 2, list_num))
#
#
# spent_time(list_num)
# # 5 Задание
# rooms = [
#     {"name": "Kitchen", "length": 6, "width": 4},
#     {"name": "Room 1", "length": 5.5, "width": 4.5},
#     {"name": "Room 2", "length": 5, "width": 4},
#     {"name": "Room 3", "length": 7, "width": 6.3},
# ]
# value = list(map(lambda item: item['length'] * item['width'], rooms))
# print("5-e задание")
# print(f"Площадь квартиры {reduce(lambda p, n: p+n, value, 0)}")
