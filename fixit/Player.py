class Player():
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.history = []

    def add_trade(self, trade):
        self.history.append(trade)

    def __str__(self):
        return "Player {} History: {} ".format(str(self.name),str(self.history))

