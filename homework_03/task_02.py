# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_function(name, surname, year, city, email, phone):
    """функция данных о пользователе"""
    return ' '.join([name, surname, year, city, email, phone])


my_name = input('Введите имя: ')
my_surname = input('Введите фамилию: ')
my_year = input('Введите год рождения: ')
my_city = input('Введите город проживания: ')
my_email = input('Введите email: ')
my_phone = input('Введите телефон: ')
print(my_function(name = my_name, surname = my_surname, year = my_year,
                  city = my_city, email = my_email, phone = my_phone))
