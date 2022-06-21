#
import datetime
#

# Programmer


class Doctor:
    def __init__(self, name: str, surname: str) -> None:
        self.__name = name
        self.__surname = surname
        self.__list_of_patient = []
        self.__availability = []

    def __repr__(self):
        return "Doctor {} {}\n {}".format(self.__name, self.__surname, self.__list_of_patient)

    def add_patient(self, patient):
        self.__list_of_patient.append(patient)

    def add_days(self, *dates):
        self.__availability.append(dates)

    def list_of_patient(self, date):
        print("Doctor {} {} patient's list for {}:\n".format(self.__name, self.__surname, date))


class Patient:
    def __init__(self, name: str, surname: str, age: int, gender: str) -> None:
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return "{} {} - {}, {} years old".format(self.__name, self.__surname, self.__gender, self.__age)



###################################

# User
p1 = Patient("Petros", "Petrosyan", 35, "M")
p2 = Patient("Martiros", "Martirosyan", 30, "M")
print(p1)


dt1 = datetime.datetime(2022, 6, 21, 9, 0)
dt2 = datetime.datetime(2022, 6, 21, 9, 30)
dtsch = {dt1: p1, dt2: p2}

d1 = Doctor("Petros", "Petrososvich")
d1.add_patient(p1)
d1.add_patient(p2)

print(d1)
