#!/usr/bin/python3


class SingletonObject(object):
    __instance = None

    class __SingletonObject:
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls.__SingletonObject()
        return cls.__instance


class SingletonObject2(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            cls.__instance = super().__new__(cls)
        return cls.__instance


class SingletonLazyInstantiation:
    __instance = None

    def __init__(self) -> None:
        if self.__instance:
            self.get_instance()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazyInstantiation()
        return cls.__instance


# instance = SingletonLazyInstantiation()
# instance = instance.get_instance()


class MonoStateSimple:
    __state = {}

    def __init__(self, *args, **kwargs):
        self.__dict__ = self.__state


# instance1 = MonoStateSimple()
# instance1.x = 20
# instance2 = MonoStateSimple()
# instance3 = MonoStateSimple()
# print(instance1.__dict__)
# print(instance2.__dict__)
# print(instance3.__dict__)


class MonoStateNew:
    __state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj


# instance1 = MonoStateNew()
# instance1.x = 20
# instance2 = MonoStateNew()
# instance3 = MonoStateNew()
# print(instance1.__dict__)
# print(instance2.__dict__)
# print(instance3.__dict__)


class MetaSingleton(type):
    __instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instance:
            self.__instance[self] = super().__call__(*args, **kwargs)
        return self.__instance[self]


class Singleton(metaclass=MetaSingleton):
    # __metaclass__ = MetaSingleton
    pass


# ob1 = Singleton()
# ob2 = Singleton()
# print(ob1, ob2)


class Test:
    def __new__(cls, *args, **kwargs):
        return cls

    def __init__(self, name=None, *args, **kwargs):
        pass

    def __call__(self, family=None, *args, **kwargs):
        pass


# test = Test(name="Masoud")
# test(family="Taee")

# test1 = Test()
# # or
# test2 = type("Test").__call__()
