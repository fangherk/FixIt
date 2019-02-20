import random
from collections import deque

from fixit.Order import Order
from fixit.MatchingEngine import MatchingEngine
from fixit.AccountingBook import AccountingBook
from fixit.Player import Player


class FixItGame:
    def __init__(self):
        self.deck = deque(list(range(1, 14)) * 4)
        self.rounds = 3
        self.middle = []
        self.engine = MatchingEngine()
        self.accounting = AccountingBook()

    def set_up_game(self, players):
        """Intialize game with players and middle cards"""
        print("\n\nShuffling Deck of {} cards".format(len(self.deck)))
        random.shuffle(self.deck)

        print("Draw Three Cards and put them in the middle")
        for _ in range(self.rounds):
            self.middle.append(self.deck.pop())

        print("Adding players to game\n\n\n")

        for name in players:
            draw_card = self.deck.pop()
            new_player = Player(name, draw_card)
            self.accounting.add_player(new_player)

        print("Displaying accounting book")
        self.stats()
        print("Set up complete\n\n\n\n")

    def stats(self):
        """Show all the players and their history"""
        for _, val in self.accounting.players.items():
            print(val)

    def play(self):
        """Game loop"""
        num_cards = len(self.accounting.players) + self.rounds
        for turn in range(1, self.rounds + 1):
            print("Total Cards in Play {}".format(num_cards))
            print("Revealing Cards: {}\n".format(self.middle[:turn]))
            while True:

                buyer = input(
                    "Press 0 to end turn. Press 1 for buy. Press 2 for sell. Press 3 for delete. \n"
                )
                if buyer == "0":
                    break

                person = input("What is your id?\n")

                # ASSUME integer values
                if buyer == "3":
                    type = input("Press 1 for bid. Press 2 for offer\n")
                    price = input("What was the price of the order?\n")
                    if type == "1":
                        self.engine.delete_order(person, int(price), "BUY")
                    else:
                        self.engine.delete_order(person, int(price), "SELL")
                    continue

                price = input("What is the price of the share?\n")

                order = Order(person, int(price), 1)

                if buyer == "1":
                    self.engine.add_order(order, "BUY")
                    self.accounting.players[person].add_order(order, "BUY")
                if buyer == "2":
                    self.engine.add_order(order, "SELL")
                    self.accounting.players[person].add_order(order, "SELL")

                #Trade = namedtuple("Trade", "seller buyer score")
                trade = self.engine.balance_orders()

                print(self.engine)
                if trade:
                    self.accounting.balance_player_orders(trade)
                    print(self.accounting)

            self.stats()

            print("Ending Round\n\n\n")
            self.engine.wipe()
        print("End Game.\n\n\n")
        self.accounting.scoring(self.middle)


def simulate_game():
    """Function to start the game"""
    game = FixItGame()
    num_players = input("How many players are there?\t")
    players = [str(x) for x in list(range(1, int(num_players) + 1))]
    game.set_up_game(players)

    start = input("Start game? (y) \t")
    if start == "y":
        game.play()
    else:
        print("No game.")


if __name__ == "__main__":
    simulate_game()
