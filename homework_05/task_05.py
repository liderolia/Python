# 5) Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

with open('task_05.txt', 'w', encoding='utf-8') as f_obj:
    num_line = input('Введите числа через пробел: ')
    f_obj.writelines(num_line)
    print(f'Сумма Ваших чисел равна {sum(map(int, num_line.split()))}')
