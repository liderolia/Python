# 1) Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_function(num_a, num_b):
    """функция нахождения частного"""
    try:
        rez = num_a / num_b
        return rez
    except ZeroDivisionError:
        return 'делить на 0 нельзя'


while True:
    try:
        number_1 = int(input('Введите первое число: '))
        number_2 = int(input('Введите второе число: '))
        break
    except ValueError:
        print('!! Вводите только числа')
print(my_function(number_1, number_2))
