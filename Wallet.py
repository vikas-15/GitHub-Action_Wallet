class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

if __name__=="__main__":
    ob1=Wallet(100)
    print(ob1.balance)
    ob1.add_cash(20)
    print(ob1.balance)
    ob1.spend_cash(80)
    print(ob1.balance)