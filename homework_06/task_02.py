# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
# оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
# что вы сделали и чего удалось добиться

from memory_profiler import profile
from random import randint

@profile
def my_function():
    '''Функция сравнения елементов списка: урок 4, задание 2'''
    my_list = [randint(0, 10000) for i in range(100000)]
    # увеличила генерацию до 100000 для наглядности
    new_lst = []
    for el in range(int(len(my_list)-1)):
        if my_list[el+1] > my_list[el]:
            new_lst.append(my_list[el+1])
            el += 1
    return new_lst

@profile
def my_function_2():
    '''Удаление генерируемого списка приводит к уменьшению выделяемой памяти'''
    my_list = [randint(0, 10000) for i in range(100000)]
    new_lst = []
    for el in range(int(len(my_list)-1)):
        if my_list[el+1] > my_list[el]:
            new_lst.append(my_list[el+1])
            el += 1
    del my_list
    return new_lst

@profile
def my_function_3():
    '''При использовании генератора "yield" мы не видим выделения памяти'''
    my_list = [randint(0, 100) for i in range(10)]
    # уменьшила генирацию для наглядности отображение работы скрипта
    new_lst = []
    for el in range(int(len(my_list)-1)):
        if my_list[el+1] > my_list[el]:
            new_lst.append(my_list[el+1])
            el += 1
    print(new_lst)
    # вывожу в печать для наглядности работы скрипта
    yield new_lst

my_function()
my_function_2()
next(my_function_3())

@profile
def my_func():
    '''Урок 4, задание 3: изменила вводные данные для наглядности отображения'''
    numbers = [randint(0, 1000) for i in range(100000)]
    new_list = [el for el in numbers if el % 100 == 0]
    return new_list

@profile
def my_func_2():
    '''Присвоила списку значение "None"'''
    numbers = [randint(0, 1000) for i in range(100000)]
    new_list = [el for el in numbers if el % 100 == 0]
    numbers = None
    return new_list

my_func()
my_func_2()
