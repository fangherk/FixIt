"""Order class"""

from datetime import datetime


class Order:
    """Class for orders made by players"""

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

    def to_dict(self):
        """returns a dictionary with self's properties"""
        out = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "time": self.time.strftime("%B %d, %Y")
        }
        return out
