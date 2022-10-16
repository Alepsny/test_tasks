'''
Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую цифру на цифру из B. Каждую цифру B можно использовать только один раз.
'''


def repl(a_list, b_max):
    for i in range(len(a_list)):
        if b_max > a_list[i]:
            a_list[i] = b_max
            return(a_list)

a, b = int(input()), int(input())
b_list = [int(i) for i in str(b)]
a_list = [int(i) for i in str(a)]
b_max = max(b_list)
print(b_list, b_max)
print(*repl(a_list, b_max), sep='')
