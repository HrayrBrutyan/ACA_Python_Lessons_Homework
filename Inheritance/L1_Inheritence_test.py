class A:
    def __init__(self, a):
        print("Constructor A start")
        self.a_value = a
        print("Constructor A end")

    def some_func(self):
        print("Some func A")
        return "Hello"


class B(A):
    def __init__(self, a, b):
        print("Constructor B start")
        super().__init__(a)
        self.b_value = b
        print("Constructor B end")

    def some_func(self):
        print("Some func B")
        super().some_func()
        return "Hello"


class C(B):
    def __init__(self, a, b, c):
        print("Constructor C start")
        super().__init__(a, b)
        self.c_value = c
        print("Constructor C end")

    def some_func(self):
        print("Some func C")
        super().some_func()
        return "Hello"


c = C(1, 2, 3)
c.some_func()
