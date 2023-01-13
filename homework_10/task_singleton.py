'Создать метакласс для паттерна Синглтон'

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyDataClass(metaclass=Singleton):
    pass

a_1  = MyDataClass()
a_2  = MyDataClass()
print(a_1, a_2)
print(a_1 == a_2)
