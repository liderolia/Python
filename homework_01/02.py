# 2) Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time = int(input("Введите время в секундах: "))
h = time // 3600
m = (time - h * 3600) // 60
s = time - (h * 3600 + m * 60)
h1 = h
m1 = m
s1 = s
if h < 10:
    h1 = '0' + str(h)
if m < 10:
    m1 = '0' + str(m)
if s < 10:
    s1 = '0' + str(s)
print(f'Время в формате "чч:мм:сс": {h1}:{m1}:{s1}')
