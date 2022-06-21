# Programmer

class Length:
    LENGTH = {"meter": 1, "foot": 0.3048, "km": 1000, "yard": 0.9144, "mile": 1609.34}

    def __init__(self, unit, val):
        self.__unit = unit
        self.__value = val

    def __str__(self):
        return "{} {}".format(self.__unit, self.__value)

    def __add__(self, other):
        x = self.__value
        if self.__unit == other.__unit:
            x += other.__value
        else:
            rate = self.LENGTH[other.__unit] / self.LENGTH[self.__unit]
            x += (rate * other.__value)
        return Length(self.__unit, x)

    def __sub__(self, other):
        x = self.__value
        if self.__unit == other.__unit:
            x -= other.__value
        else:
            rate = self.LENGTH[other.__unit] / self.LENGTH[self.__unit]
            x -= (rate * other.__value)
        if x < 0:
            return False
        return Length(self.__unit, x)


###################################

# User

u1 = Length("meter", 100)
# print(u1)
u2 = Length("meter", 500)
# print(u2)
u3 = u1 + u2 + u2
print(u3)

u4 = Length("km", 4)
# print(u4)
print(u3 + u4)
print(u4 + u1)
print(u4 - u1)