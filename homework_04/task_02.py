# 2) Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

# Функции my_function и my_function_2 сравнивают 0 элемент списка с последним
# и выводит его, если он больше.
def my_function(my_lst):
    '''Функция сравнения елементов списка'''
    i = 0
    new_lst = []
    for el in my_lst:
        if el > my_lst[i-1]:
            new_lst.append(el)
        i += 1
    yield new_lst


def my_function_2(my_lst):
    '''Вариант 2: в одну строку'''
    new_lst = [el for el in my_lst if el > my_lst[my_lst.index(el)-1]]
    yield new_lst


def my_func(lst):
    '''Функция сравнения елементов списка, без сравнения 0 и последнего'''
    new_lst = []
    for el in range(int(len(lst)-1)):
    # Использовала range(int(len(lst)), т.к. мне нужна длина списка -1 ед.
        if lst[el+1] > lst[el]:
            new_lst.append(lst[el+1])
            el += 1
    yield new_lst


my_list = [randint(0, 100) for i in range(10)]
print(my_list)
print(f'Вариант 1: {next(my_function(my_list))}')
print(f'Вариант 2: {next(my_function_2(my_list))}')
print(f'Вариант 3: {next(my_func(my_list))}')
