def cycle_subs(num, subs):
    inner_cycle = num
    count = 0
    while num > 0:
        for i in subs:
            if count < inner_cycle:
                yield i
            else:
                break
            count += 1
        num -= 1


while True:
    try:
        user_input = int(input("Из скольки чисел будет последовательность? "))
        user_input_num = input('Укажите последовательность чисел ')
        a = cycle_subs(user_input, user_input_num)
        arr = []
        for j in a:
            arr.append(str(j))
        print('-'.join(arr))
        break
    except ValueError as error:
        print('Ввели не число')
