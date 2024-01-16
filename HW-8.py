import random
import time

# def imt_chek(imt: float):
#     imt_f = f"{imt:.2f}"
#     print(f"{imt_f} - Выраженный дефицит массы тела") if imt <= 16 else ''
#     print(f"{imt_f} - Недостаточная(дефицит) масса тела") if 16 < imt <= 18.5 else ''
#     print(f"{imt_f} - Норма") if 18.5 <= imt <= 24.99 else ''
#     print(f"{imt_f} - Избыточная масса тела(предожирение)") if 25 <= imt <= 30 else ''
#     print(f"{imt_f} - Ожирение первой степени") if 30 < imt <= 35 else ''
#     print(f"{imt_f} - Ожирение второй степени") if 35 < imt <= 40 else ''
#     print(f"{imt_f} - Ожирение третьей степени(морбидное)") if 40 < imt else ''
#
#
# def imt(weight: int, height: int) -> int:
#     res = weight / (height / 100) ** 2
#     imt_chek(res)
#
# print("Давайте рассчитаем ваш индекс массы тела")
# while True:
#     try:
#         weight = int(input("Введите Ваш вес в кг: "))
#         height = int(input("Введите Ваш рост в см: "))
#         imt(weight, height)
#         break
#     except ValueError as error:
#         print(f"Введены некоректные данные {error}")


# class Calc:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(f"Результат операции сложения {self.a} + {self.b} = {self.a + self.b}")
#
#     def sub(self):
#         print(f"Результат операции вычитания {self.a} - {self.b} = {self.a - self.b}")
#
#     def div(self):
#         print(f"Результат операции деления {self.a} / {self.b} = {(self.a / self.b):.2f}")
#
#     def mul(self):
#         print(f"Результат операции умножения: {self.a} * {self.b} = {(self.a * self.b):.2f}")
#
#
# while True:
#     try:
#         first_value = float(input('Введите первое число: '))
#         second_value = float(input('Введите второе число: '))
#         operation = input("Введите операцию '+' '-' '*' '/': ")
#         while operation != '+' and operation != '-' and operation != '/' and operation != '*':
#             print('Такой операции не существует')
#             operation = input("Введите операцию '+' '-' '*' '/': ")
#
#         res = Calc(first_value, second_value)
#         if operation == '+':
#             res.add()
#             break
#         elif operation == '-':
#             res.sub()
#             break
#         elif operation == '/':
#             try:
#                 res.div()
#                 break
#             except ZeroDivisionError as err:
#                 print(f"Деление на ноль запрещено, {err}")
#         else:
#             res.mul()
#             break
#     except ValueError as err:
#         print("Ввели не число")
# list_1 = [3, 5, 6, 3, 7, 8]
# list_2 = [item%3 for item in list_1]
# print(list_2)
# value = 'dsa'
# print(f"Число") if isinstance(value, int) else print(f"Не число")