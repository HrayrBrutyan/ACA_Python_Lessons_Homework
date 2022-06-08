#
import random
import string

#
from L1_Time_class import Date
from L2_Person_class import Person
from L3_Money_class import Money


class BankAccount:
    def __init__(self, p: Person, m: Money, vt: Date) -> None:
        self.__customer = p
        self.__account_number = ''.join(random.choices(string.digits, k=16))
        self.__balance = m
        self.__valid_till = vt

    #TODO: get and set for all members
    def get_person(self):
        return self.__customer

    def get_account(self):
        return self.__account_number

    def get_money(self):
        return self.__balance

    def get_date(self):
        return self.__valid_till

    def __str__(self) -> str:
        return "Personal info --- {}\nAccount number --- {}\nBalance --- {}".format(self.__customer, self.__account_number, self.__balance)

    def deal(self, m):
        x = self.__balance - m
        if x:
            self.__balance = x
            print("Deal approved. Your current balance is {}".format(x))
        else:
            print("Sorry. Balance is not enough.")

    def fill_balance(self, m):
        self.__balance += m
        print("Congratulations!!! Balance successfully filled!!!\nYour current balance is {}".format(self.__balance))

    def update(self, n):
        self.__valid_till.add_year(n)

    def deposite(self, m, d, p):
        # money, duration, percent
        # TODO: count many after duration with p percent
        pass


###################################

# User

p = Person("Hrayr", "Brutyan", 32, "Male")
m = Money("USD", 1000)
vt = Date(2022, 6, 9)

ba = BankAccount(p, m, vt)
# print(ba)

m1 = Money("RUB", 1500)
m2 = Money("EUR", 250)
# ba.deal(m1)
# print(ba)

ba.fill_balance(m2)
print(ba)



