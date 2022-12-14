# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

def my_sum():
    """Программа выполнена: True"""
    sum_res = 0
    my_program = False
    while my_program is False:
        number = input('Вводите числа через пробел, (ВЫХОД = Q): ').split()
        result = 0
        for el in number:
            if el in ('q', 'Q'):
                my_program = True
                break
            result = result + int(el)
        sum_res = sum_res + result
        print(f'Сумма всех чисел = {sum_res}')
    print('Конец программы')

my_sum()
