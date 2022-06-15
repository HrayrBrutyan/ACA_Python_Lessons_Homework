from abc import ABC, abstractmethod


class Template(ABC):
    @abstractmethod
    def my_abstract_method(self, x):
        return "Abstract"

    @abstractmethod
    def my_abstract_method_1(self, x):
        pass

    @abstractmethod
    def my_abstract_method_2(self, x):
        pass

    @abstractmethod
    def my_abstract_method_3(self, x):
        pass

    @abstractmethod
    def my_abstract_method_4(self, x):
        pass

    def my_method(self, a, b):
        pass


class Main(Template):

    def __init__(self, v1):
        self.value = v1
        return None

    def my_abstract_method(self, y):
        x = super().my_abstract_method(y)
        print("CALL - ", x)
        return None

    def my_abstract_method_1(self, x):
        pass

    def my_abstract_method_2(self, x):
        pass

    def my_abstract_method_3(self, x):
        pass

    def my_abstract_method_4(self, x):
        pass


m = Main("Abstract")
x = m.my_abstract_method(8)
print("X", x)


