class Person:

    def __init__(self, fn, ln, a, g):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.gender = g

    def __str__(self):
        # print("Person")
        return "{} {} - {}, {}".format(self.first_name, self.last_name, self.age, self.gender)


class Student(Person):
    def __init__(self, fn, ln, a, g, univ, fac):
        super().__init__(fn, ln, a, g)
        self.university = univ
        self.faculty = fac

    def __str__(self):
        print("Student")
        return "{}, faculty of {}\n".format(self.university, self.faculty) + super().__str__()


###################################

# User

# s = Student("Julia", "Smith", 32, "Female", "YSU", "Informatics and Applied Mathematics")
# print(s)





