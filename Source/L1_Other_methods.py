class Student:
    def __init__(self, work, score):
        self.__work = work
        self.score = score

    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        # object.__setattr__(self, key, value) The two statements are equivalent

    def __delattr__(self, name):
        print("You are deleting an attribute")
        return super().__delattr__(name)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def valod(self):
        pass


s = Student("YSU", 4)



