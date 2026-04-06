# 4. Bank Account System (Class, Object, Constructor) A bank wants to manage customer accounts. Create a BankAccount class with a constructor to initialize account number and balance. Implement methods to deposit, withdraw, and display balance.

class BankAccount:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal
        print
        print("Intial Balance was ",bal)
    def deposite(self,amount):
        if amount>0:
            self.bal=self.bal+amount
            print("Deposited amount is ",amount)

    def withdraw(self,amount):
        print("Withdrawn amount is ",amount)
        if amount>0:
            self.bal=self.bal-amount

    def balance(self):
        print("Balance after transaction is",self.bal)

a=BankAccount("BANK0011",2000)
a.deposite(500)
a.withdraw(250)
a.balance()

