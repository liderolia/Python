# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени,
# оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
# что вы сделали и чего удалось добиться
from timeit import timeit
from random import randint

print('скрипт №1:')
'''сортировка списка быстрее, чем сравнивание отдельных элементов между собой'''
def my_func(num_1, num_2, num_3):
    '''сравнивание элементов между собой'''
    my_string = [num_1, num_2, num_3]
    total = []
    max_1 = max(my_string)
    total.append(max_1)
    my_string.remove(max_1)
    max_2 = max(my_string)
    total.append(max_2)
    return f'{max_1} + {max_2} = {sum(total)}'

def my_func_new(num_1, num_2, num_3):
    '''сортировка списка'''
    my_string = [num_1, num_2, num_3]
    my_string.sort()
    return f'{my_string[-2]}+{my_string[-1]}={my_string[-2] + my_string[-1]}'

print(timeit("my_func(5, 15, 10)",  globals=globals(), number=1000))
print(timeit("my_func_new(5, 15, 10)",  globals=globals(), number=1000))

print()
print('скрипт №2:')
def my_function(n):
    '''создание дополнительных переменных увеличивает время обработки'''
    n1 = int(n)
    n2 = int(n + n)
    n3 = int(n + n + n)
    return f'{n1} + {n2} + {n3} = {n1 + n2 + n3}'

def my_function_2(n):
    return f'{n} + {n}{n} + {n}{n}{n} = {int(n) + int(n + n) + int(n + n + n)}'

print(timeit("my_function('5')",  globals=globals(), number=10000))
print(timeit("my_function_2('5')",  globals=globals(), number=10000))

print()
print('скрипт №3:')

def my_func():
    '''создание списка увеличивает время обработки'''
    numbers = list(range(10, 100))
    new_list = [el for el in numbers if el % 10 == 0]
    return new_list
def my_func_2():
    return [el for el in range(10, 100) if el % 10 == 0]

print(timeit("my_func()",  globals=globals()))
print(timeit("my_func_2()",  globals=globals()))
