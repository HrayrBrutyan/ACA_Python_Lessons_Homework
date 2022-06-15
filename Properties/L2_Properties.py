class Rational:

    def __init__(self, n, d):
        x = Rational.gcd(n, d)
        self.__nominator = n // x
        self.__denominator = d // x

    def __repr__(self):
        return "{}/{}".format(self.__nominator, self.__denominator)

    @classmethod
    def create_obj(cls, s):
        a = s.split('/')
        return cls(int(a[0]), int(a[1]))

    @staticmethod
    def gcd(x, y):
        c = 1
        for i in range(2, min(x, y) + 1):
            if x % i == 0 and y % i == 0:
                c = i
        return c

    def get_nominator(self):
        print("GET")
        return self.__nominator

    def get_denominator(self):
        print("GET")
        return self.__denominator

    def set_nominator(self, x):
        print("SET")
        if x > 0:
            y = Rational.gcd(x, self.__denominator)
            self.__nominator = x // y
            self.__denominator = self.__denominator // y

    nominator = property(get_nominator, set_nominator)

    def __add__(self, other):
        x = self.nominator * other.denominator + self.denominator * other.nominator
        y = self.denominator * other.denominator
        return Rational(x, y)


r = Rational(4, 6)
print(r)
r.nominator = 15
print(r)

