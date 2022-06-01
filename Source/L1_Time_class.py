# Programmer
class TimeError(Exception):
    def __init__(self, msg, val):
        self.__message = "{} value out of range".format(msg)
        self.__value = val

    def get_message(self):
        return self.__message

    def get_value(self):
        return self.__value


class Time:
    def __init__(self, h, m, s):
        try:
            if h < 0 or h > 23:
                raise TimeError("Hour", h)
            if m < 0 or m > 59:
                raise TimeError("Minute", m)
            if s < 0 or s > 59:
                raise TimeError("Second", s)
        except TimeError as err:
            print(err)
        else:
            self.__hour = h
            self.__minute = m
            self.__second = s
            # finally:
        #    print("Object creation process")

    def __repr__(self): #__repr__ kam __str__ magic ֆուկցիաները օգտագործելիս self-ին ատրիբուտներ չի տրվում և միայն տպում է։
        # Function that adds 0 if any value is < 10
        h = self.__hour
        m = self.__minute
        s = self.__second

        if h < 10:
            h = f"0{h}"
        if m < 10:
            m = f"0{m}"
        if s < 10:
            s = f"0{s}"
        return "{}:{}:{}".format(h, m, s)

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def set_hour(self, x):
        if x > 0 and x < 23:
            self.__hour = x
            print("Value successfully changed")
        else:
            print("Sorry: Invalid value")

    def add_hour(self, h):
        try:
            if not isinstance(h, int):  # checks parametr type
                raise TimeError("Hour", h)
        except TimeError as err:
            print(err)
        else:
            self.__hour = (self.__hour + h) % 24

    def add_minute(self, m):
        x = self.__minute + m
        self.__minute = x % 60
        self.add_hour(x // 60)

    def add_second(self, s):
        x = self.__second + s
        self.__second = x % 60
        self.add_minute(x // 60)


# User

# t = Time(9, 5, 40)
# print(t)
# print(t.get_second())
# t.set_hour(28)  # Sorry: Invalid value
# t.set_hour(8)  # Value successfully changed
# print(t)
#
# t.add_hour("55")
# t.add_hour(5)
# print(t)
# t.add_second(5005)
# print(t)
# t.add_minute(55)
# print(t)


########################################################################################################################


# Programmer
class DateError(Exception):
    def __init__(self, msg, val, fn):
        self.__message = msg
        self.__value = val
        self.__function_name = fn

    def get_info(self):
        return "{} value out of range {} - {}".format(self.__message, self.__value, self.__function_name)

    def get_value(self):
        return self.__value


class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        try:
            if y < 0:
                raise DateError("Year", y, 'constructor')
            if m < 1 or m > 12:
                raise DateError("Month", m, 'constructor')
            if d < 1 or d > Date.MONTH_DAYS[m]:
                raise DateError("Day", d, 'constructor')
        except DateError as err:
            print(err.get_info())
        else:
            self.__year = y
            self.__month = m
            self.__day = d

    def __str__(self):
        # Function that adds 0 if any value is < 10
        m = self.__month
        d = self.__day

        if m < 10:
            m = f"0{m}"
        if d < 10:
            d = f"0{d}"
        return "{}/{}/{}".format(self.__year, m, d)

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def add_year(self, y):
        self.__year += y

    # def add_month(self, m):
    #     x = self.__month + m
    #     if x <= 12:
    #         self.__month = x
    #     elif x % 12 != 0:
    #         self.__month = x % 12
    #         self.add_year(x // 12)
    #     elif x % 12 == 0:
    #         self.__month = 12
    #         self.add_year((x // 12) - 1)

    def add_month(self, m):
        x = self.__month + m
        self.__month = ((x - 1) % 12) + 1
        self.add_year((x - 1) // 12)

    # def add_day(self, d):
    #     x = self.__day + d
    #     counter = 0
    #     while x > self.MONTH_DAYS[self.__month]:
    #         x = x - self.MONTH_DAYS[self.__month]
    #         self.__month += 1
    #         if self.__month == 13:
    #             self.__month = 1
    #             counter += 1
    #     self.__day = x
    #     self.add_year(counter)

    def add_day(self, d):
        x = self.__day + d
        while x > self.MONTH_DAYS[self.__month]:
            x = x - self.MONTH_DAYS[self.__month]
            self.add_month(1)
        self.__day = x

    def __check_month_value(self, m):
        if m < 0 or m > 12:
            return False
        return True

    def set_month(self, m):
        try:
            if not self.__check_month_value(m):
                raise DateError("Month", m, 'set month')
        except DateError as err:
            print(err.get_info())
        else:
            self.__month = m


# User

d1 = Date(2022, 5, 26)
print(d1)
d1.add_day(220)
print(d1)

d1.set_month(13)


########################################################################################################################


# Programmer
class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} - {}".format(self.__date, self.__time)

    # def add_year(self, y):
    #    self.__date.add_year(y)

    def add_month(self, m):
        self.__date.add_month(m)

    def add_day(self, d):
        self.__date.add_day(d)

    def add_minute(self, m):
        self.__time.add_minute(m)

    def add_second(self, s):
        self.__time.add_second(s)

    def add_hour(self, h):
        x = self.__time.get_hour() + h
        self.__time.add_hour(x % 24)
        self.__date.add_day(x // 24)


print("Below is from DateTime class")
d2 = Date(2022, 5, 8)
print(d2)
t2 = Time(7, 5, 50)
print(t2)


dt = DateTime(d2, t2)
print(dt)
print("Add month")
dt.add_month(8)
print(dt)
dt.add_minute(85)
print(dt)
dt.add_day(855)
print(dt)

# a = Date.MONTH_DAYS
# for i in range(len(a)):
#     print(f"{i}: month has {a[i]} days")




