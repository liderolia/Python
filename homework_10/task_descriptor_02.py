class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = '_' + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError('Невозможно удалить атрибут')


class Road:
    _length = TypedProperty('_length', float)
    _width = TypedProperty('_width', float)
    weight = TypedProperty('weight', float)
    depth = TypedProperty('depth', float)

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def weight_road(self):
        return self._length * self._width * self.weight * self.depth/1000

result = Road(20.0, 5000.0, 25.0, 0.05)
print(f'Необходимо {result.weight_road()} тонн асфальта')

result_2 = Road(20.0, '5000.0', 25.0, 0.05)
print(f'Необходимо {result_2.weight_road() / 1000} тонн асфальта')
