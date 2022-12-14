# 2) Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длинаширинамасса асфальта
# для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def weight_road(self):
        '''В условиях задачи неверный расчет в приведенном примере:
        нельзя перемножать длину в метрах и сантиметрах одновременно,
        надо всё привести к одинаковой системе измерения'''
        return self._length * self._width * self.weight * self.depth

result = Road(20, 5000, 25, 0.05)
print(f"Необходимо {result.weight_road() / 1000} тонн асфальта")
