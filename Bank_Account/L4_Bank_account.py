#
import random
import string

#
from Bank_Account.L1_Time_class import Date
from Bank_Account.L2_Person_class import Person
from Bank_Account.L3_Money_class import Money


class BankAccount:
    def __init__(self, p: Person, m: Money, vt: Date) -> None:
        self.__customer = p
        self.__account_number = ''.join(random.choices(string.digits, k=16))
        self.__balance = m
        self.__valid_till = vt

    #TODO: get and set for all members
    def get_customer(self):
        return self.__customer

    def get_account(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_valid(self):
        return self.__valid_till

    def set_customer(self, p):
        self.__customer = p

    def set_balance(self, m):
        self.__balance = m

    def set_valid(self, vt):
        self.__valid_till = vt

    def __str__(self) -> str:
        return "Personal info --- {}\nAccount number --- {}\nBalance --- {}\nValid till --- {}".\
            format(self.__customer, self.__account_number, self.__balance, self.__valid_till)

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
        # money, duration in months, percent
        if self.__balance - m:
            self.__balance += m * ((p/100)/12*d)
            print("Your balance after {} months with {} percent will be {}".format(d, p, self.__balance))
        else:
            print("Sorry, you can't make a deposit ({}), which is larger than your balance ({})".format(m, self.__balance))




###################################

# User

p = Person("Hrayr", "Brutyan", 32, "Male")
m = Money("USD", 1000)
vt = Date(2022, 6, 9)

ba = BankAccount(p, m, vt)
# print(ba)

m1 = Money("USD", 100)
ba.deal(m1)
# print(ba)

m1 = Money("RUB", 20000)  # 20,000 RUB = 200 USD
ba.deal(m1)
# print(ba)

m2 = Money("EUR", 500)  # 500 EUR = 600 USD
ba.fill_balance(m2)
# print(ba)

m3 = Money("EUR", 2000)  # 2,000 EUR = 2,400 USD

ba.deposite(m1, 6, 10)
ba.deposite(m2, 6, 8)
ba.deposite(m3, 6, 6)

