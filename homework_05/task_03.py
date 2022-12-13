# 3) Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто
# из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task_03.txt', "r", encoding='utf-8') as my_list:
    print('\033[1m\033[4mЗарплата меньше 20000 руб.:\033[0m')
    person_list = my_list.readlines()
    salary = 0
    new_list = []
    for el in person_list:
        new_list = list(el.split())
        salary += float(new_list[1])
        if float(new_list[1]) < 20000:
            print(f'{new_list[0]}: {new_list[1]} руб.')
    print()
    print(f'\033[1mСредняя з/п сотрудников =\033[0m'
          f'{salary / len(person_list)}')
