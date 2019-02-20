class Player():
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.history = []
        self.bids = []
        self.offers = []

    def add_trade(self, trade):
        """Adds completed transaction to history of player"""
        #Score = namedtuple("Score", "pot_value num_shares party")
        self.history.append(trade)

    def add_order(self, order, order_type="BUY"):
        """Adds bid or offer by player to the players bids or offers"""
        book = self.bids if order_type == "BUY" else self.offers
        book.append(order)

    def show_orders(self):
        """Represents a players bids and offers in a table"""
        ## TODO: implement show Orders
        return

    def __str__(self):
        return "Player {} History: {} ".format(
            str(self.name), str(self.history))
