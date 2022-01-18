class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, deposit):
        self.balance += deposit
        print(f"I deposit to you account:\n{deposit}$")

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"I withdraw from your bank account:\n{withdraw}$")
        else:
            print("On your bank account ot enough money")

    def show_account(self):
        print(f"On the account:\n{self.balance}$")


bank_account_1 = Bank()

print("I open a bank account")
bank_account_1.deposit(10000)
bank_account_1.show_account()
bank_account_1.withdraw(4900)
bank_account_1.show_account()
