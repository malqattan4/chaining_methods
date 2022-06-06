from distutils.archive_util import make_archive


class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0


    def make_withdrawal(self, amount):
        self.make_withdrawal-=amount
        return self


    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account_balance}")
        return self


    def make_deposite(self,amount):
        self.account_balance+=amount
        return self



Maryam=user("Maryam", "m@gmail.com")
Abeer =user("Abeer", "abeer@yahoo.com")
Hettaf=user("Hettf", "halqattan@live.com")

Maryam.make_deposite(2000).make_deposite(300).make_deposite(450).make_withdrawal(260).display_user_balance()

Abeer.make_deposite(4500).make_deposite(200).make_withdrawal(50).make_withdrawal(200).display_user_balance()

Hettaf.make_deposite(3700).make_withdrawal(450).make_withdrawal(100).make_withdrawal(200).display_user_balance()