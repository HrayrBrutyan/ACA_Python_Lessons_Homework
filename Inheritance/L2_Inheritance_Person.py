class Person:

    def __init__(self, fn, ln, a, g):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        self.gender = g

    def __str__(self):
        print("Person")
        return "{} {} - {},{}".format(self.first_name, self.last_name, self.age, self.gender)


class Teacher(Person):
    def __init__(self, fn, ln, a, g, prof, exp):
        super().__init__(fn, ln, a, g)
        self.profession = prof
        self.experience = exp

    def __str__(self):
        print("Teacher")
        return "{}\n{} --- {}".format(super().__str__(), self.profession, self.experience)


t = Teacher("Hrayr", "Brutyan", 32, "Male", "Programmer", 1)
print(t)