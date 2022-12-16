# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
# оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
# что вы сделали и чего удалось добиться
from timeit import timeit


def my_func(num_1, num_2, num_3):
    """функция суммы 2-х наибольших аргументов: урок 3, задание 3"""
    my_string = [num_1, num_2, num_3]
    total = []
    max_1 = max(my_string)
    total.append(max_1)
    my_string.remove(max_1)
    max_2 = max(my_string)
    total.append(max_2)
    return f'{max_1} + {max_2} = {sum(total)}'

def my_func_new(num_1, num_2, num_3):
    """сортирую список и складываю 2 последних элемента"""
    my_string = [num_1, num_2, num_3]
    my_string.sort()
    return f'{my_string[-2]}+{my_string[-1]}={my_string[-2] + my_string[-1]}'

print('скрипт №1:')
print(timeit("my_func(5, 15, 10)",  globals=globals(), number=1000))
print(timeit("my_func_new(5, 15, 10)",  globals=globals(), number=1000))


def my_function(n):
    """сумма чисел n+nn+nnn ('n' вводилась как строка): урок 1, задание 3"""
    n1 = int(n)
    n2 = int(n + n)
    n3 = int(n + n + n)
    return f'{n1} + {n2} + {n3} = {n1 + n2 + n3}'

def my_function_2(n):
    """конвертация строки в числовое значение без создания доп. переменных"""
    return f'{n} + {n}{n} + {n}{n}{n} = {int(n) + int(n + n) + int(n + n + n)}'

print()
print('скрипт №2:')
print(timeit("my_function('5')",  globals=globals(), number=10000))
print(timeit("my_function_2('5')",  globals=globals(), number=10000))
