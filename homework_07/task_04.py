# 4) Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


    def go(self):
        if self.speed > 0:
            print(f'{self.color} {self.name} начала двиджение')

    def stop(self):
        if self.speed == 0:
            print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        if self.speed > 0:
            print(f'повернула на {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')

    def police(self):
        if self.is_police:
            print('Выехала полицейская машина')


class TownCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed}км/ч')
            print(f'!ВНИМАНИЕ превышение скорости на {self.speed - 60} км/ч')
            self.is_police = True
        else:
            print(f'Скорость {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости: скорость {self.speed}км/ч')
            print(f'!ВНИМАНИЕ превышение скорости на {self.speed - 40} км/ч')
            self.is_police = True
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        print(f'Полицейская машина {self.color} {self.name}: движится к нарушителю со скоростью {self.speed} км/ч')


kia = TownCar(85, 'черный', 'kia')
lada = WorkCar(35, 'серый', 'Lada')
Lamborghini = SportCar(0, 'желтый', 'Lamborghini')

kia.go()
kia.stop()
kia.turn('направо')
kia.show_speed()
kia.police()
print()
lada.go()
lada.stop()
lada.turn('налево')
lada.show_speed()
lada.police()
print()
Lamborghini.go()
Lamborghini.stop()
Lamborghini.turn('нараво')
Lamborghini.show_speed()
print()
Hyundai = PoliceCar(110, 'белый', 'Hyundai')
