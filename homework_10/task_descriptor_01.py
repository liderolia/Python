'''Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ'''

class NonNegative:

    def __init__(self, my_road):
        self.my_road =my_road

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_road]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        instance.__dict__[self.my_road] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_road]



class Road:
    _length = NonNegative('length')
    _width = NonNegative('width')
    weight = NonNegative('weight')
    depth = NonNegative('depth')

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def weight_road(self):
        return self._length * self._width * self.weight * self.depth/1000


result = Road(20, 5000, 25, 0.05)
print(f'Необходимо {result.weight_road()} тонн асфальта')

result_2 = Road(-20, 5000, 25, 0.05)
print(f'Необходимо {result_2.weight_road()} тонн асфальта')
