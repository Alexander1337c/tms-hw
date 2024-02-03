def fib_subs(num):
    list_num = [0, 1]
    while num > 0:
        yield list_num[-1]
        list_num.append(list_num[-1] + list_num[-2])
        num -= 1


try:
    user_input = int(input("До какого числа в последовательности вывести числа Фиббоначи "))
    a = fib_subs(user_input)
    print(list(a))
except ValueError as error:
    print('Ввели не число')
