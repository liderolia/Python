# 3) Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    """функция суммы 2-х наибольших аргументов"""
    my_string = [num_1, num_2, num_3]
    total = []
    max_1 = max(my_string)
    total.append(max_1)
    my_string.remove(max_1)
    max_2 = max(my_string)
    total.append(max_2)
    return f'{max_1} + {max_2} = {sum(total)}'


while True:
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        number_3 = int(input("Введите третье число: "))
        break
    except ValueError:
        print('!! Вводите только числа')
print(my_func(number_1, number_2, number_3))
