class Person:
    def __init__(self, fn, age):
        self.full_name = fn
        self.age = age
        self.gender = None

    def __str__(self):
        print("Person")
        if self.gender == "Female":
            return "{} - {}".format(self.full_name, self.gender)
        else:
            return "{} - {}, {}".format(self.full_name, self.age, self.gender)


class Student(Person):
    def __init__(self, fn, a, univ, fac):
        super().__init__(fn, a)
        self.university = univ
        self.faculty = fac

    def __str__(self):
        print("Student")
        return "{}, faculty of {}\n".format(self.university, self.faculty) + super().__str__()


s = Student("Julia Smith", 32, "YSU", "Informatics and Applied Mathematics")
print(s)





