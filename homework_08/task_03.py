'''Задание 3.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.'''

class Zerodiv(Exception):
    def __init__(self, text):
        self.text = text

def my_ZeroDivision():
    try:
        dividend = int(input('Введите делимое: '))
        divider = int(input('Введите делитель: '))
        if divider == 0:
            raise Zerodiv(divider)
        else:
            return dividend / divider
    except Zerodiv as err:
        return f'делить на {err} нельзя'

print(my_ZeroDivision())
