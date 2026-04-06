"""11. Payment System (Runtime Polymorphism)
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type."""

class Payment:
    def process_payment(self,amount):
        print("Recieved Payment in cash ",amount)

class CreditCard(Payment):
    def process_payment(self,amount):
        print("Recieved Credit Card payment of",amount)

class UPI(Payment):
    def process_payment(self,amount):
        print("Recieved UPI payment of",amount)

class NetBanking(Payment):
    def process_payment(self,amount):
        print("Recievec Net Banking payment of",amount)

cc = CreditCard()
u = UPI()
nb = NetBanking()

cc.process_payment(100)
u.process_payment(200)
nb.process_payment(300)
