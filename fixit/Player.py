class Player():
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.history = []
        self.bids = []
        self.offers = []

    def list_objects_to_dict(objects=[]):
        """Takes of a list of objects and converts it to a json {key:value} = id: {object's json} pair"""
        out = {}
        for i in range(len(objects)):
            out[str(i)] = objects[i].to_dict()
        return out

    def to_dict(self):
        """returns json dictionary for the players properties"""
        out = {
            "name": self.name,
            "card": self.card,
            "history": list(map(lambda x: [x[0], x[1], x[2]], self.history)),
            "bids": list(map(lambda x: x.price, self.bids)),
            "offers": list(map(lambda x: x.price, self.offers)),
        }

        return out

    def add_trade(self, trade):
        """Adds completed transaction to history of player"""
        #Score = namedtuple("Score", "pot_value num_shares party")
        self.history.append(trade)

    def add_order(self, order, order_type="BUY"):
        """Adds bid or offer by player to the players bids or offers"""
        book = self.bids if order_type == "BUY" else self.offers
        book.append(order)

    def delete_order(self, price, order_type="BUY"):
        """Deletes bid or offer by player"""
        book = self.bids if order_type == "BUY" else self.offers

        for i in range(len(book) - 1, -1, -1):
            current_order = book[i]
            if current_order.price == price:
                book.pop(i)
                break

    def show_orders(self):
        """Represents a players bids and offers in a table"""
        ## TODO: implement show Orders
        return

    def __str__(self):
        return "Player {} History: {} ".format(
            str(self.name), str(self.history))
