from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def makePayment(self):
        pass


# Child Class
class MobileMoneyPayment(Payment):
    def makePayment(self):
        print("Payment made using Mobile Money")


# Child Class
class CardPayment(Payment):
    def makePayment(self):
        print("Payment made using Bank Card")


# Main Program
mobile = MobileMoneyPayment()
card = CardPayment()

mobile.makePayment()
card.makePayment()