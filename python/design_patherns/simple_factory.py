#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class SimpleFactory(metaclass=ABCMeta):
    # __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class Factory(SimpleFactory):
    def execute(self):
        print("factory execute method called")


class GlobalFactory:
    def factory(self, factory_class):
        return eval(factory_class)().execute()


if __name__ == "__main__":
    global_factory = GlobalFactory()
    global_factory.factory("Factory")
