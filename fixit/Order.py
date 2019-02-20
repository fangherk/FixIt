from datetime import datetime


class Order:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.time = datetime.utcnow()

    def __repr__(self):
        return "Name:{}-Price:{}-Qty:{}-Time:{}".format(
            self.name, self.price, self.quantity, self.time)

    def __str__(self):
        return "Name:{}-Price:{}-Qty:{}-Time:{}".format(
            self.name, self.price, self.quantity, self.time)
