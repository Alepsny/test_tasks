'''
Отсортировать числа в массиве согласно сумме их цифр.
'''


def make_dict(mas):
    mas_d = dict()
    for i in mas:
        mas_d[i] = sum(map(int, list(i)))
    return mas_d

mas = [i for i in input().split()]
mas_d = make_dict(mas)
mas_sort = list(map(lambda x: x[0], sorted(mas_d.items())))
print(*mas_sort)
