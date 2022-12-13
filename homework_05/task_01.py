# 1) Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('task_01.txt', 'w', encoding = 'utf-8') as f_obj:
    while True:
        my_line = input('Введите данные: ')
        if not my_line:
            break
        f_obj.writelines(f'{my_line} \n')
