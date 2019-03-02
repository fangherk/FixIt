"""Contains FixItGame class"""

import random
from collections import deque
from random import choice

from AccountingBook import AccountingBook
from MatchingEngine import MatchingEngine
from Order import Order
from Player import Player


class FixItGame:
    """Object for playing fix it"""

    def __init__(self):
        self.deck = deque(list(range(1, 14)) * 4)
        self.rounds = 3
        self.middle = []
        self.engine = MatchingEngine()
        self.accounting = AccountingBook()

    def new_game(self, players=None):
        """Start a new game"""

        if not players:
            try:
                num_players = 3  #int(input("How many players are there?\t"))
            except:
                raise ValueError("Invalid number of players")
            else:
                players = [
                    str(x) for x in list(range(1,
                                               int(num_players) + 1))
                ]

        self.set_up_game(players)

    def set_up_game(self, players):
        """Intialize game with players and middle cards"""
        print("\n\nShuffling Deck of {} cards".format(len(self.deck)))
        random.shuffle(self.deck)

        print("Draw Three Cards and put them in the middle")
        for _ in range(self.rounds):
            self.middle.append(self.deck.pop())

        print("Adding players to game\n\n\n")

        for name in players:
            draw_card = str(self.deck.pop()) + choice([
                "D", "S", "H", "C"
            ])  # simulate the card having a certain suite until
            new_player = Player(name, draw_card)
            self.accounting.add_player(new_player)

        print("Displaying accounting book")
        self.stats()
        print("Set up complete\n\n\n\n")

    def stats(self):
        """Show all the players and their history"""
        for _, val in self.accounting.players.items():
            print(val)

    def delete_order(self, person, price, order_type):
        """ Delete an order """
        self.engine.delete_order(person, price, order_type)
        self.accounting.players[person].delete_order(price, order_type)

    def add_order(self, person, price, order_type):
        """ Add an order """
        order = Order(person, price, 1)
        self.engine.add_order(order, order_type)
        trade = self.engine.balance_orders()
        if trade:
            print("here}")
            self.accounting.balance_player_orders(trade)
        else:
            self.accounting.players[person].add_order(order, order_type)

    def play(self):
        """Game loop"""
        num_cards = len(self.accounting.players) + self.rounds
        for turn in range(1, self.rounds + 1):
            print("Total Cards in Play {}".format(num_cards))
            print("Revealing Cards: {}\n".format(self.middle[:turn]))
            while True:

                try:
                    buyer = int(
                        input(
                            "\nPress:\n0 - end turn\n1 - buy\n2 - sell\n3 - delete order\n"
                        ))
                except (SyntaxError, ValueError):
                    print("Please input an integer value")
                    continue

                if not buyer:
                    break
                elif buyer in (1, 2):
                    try:
                        person = int(input("What is your id?\n"))
                        price = int(input("What is the price of the share?\n"))
                    except (SyntaxError, ValueError):
                        print("Try Again.")
                        continue
                    else:
                        if buyer == 1:
                            self.add_order(person, price, "BUY")
                        if buyer == 2:
                            self.add_order(person, order, "SELL")
                elif buyer == 3:
                    try:
                        order_type = int(
                            input("Press 1 for bid. Press 2 for offer\n"))
                        price = int(
                            input("What was the price of the order?\n"))

                    except:
                        raise ValueError("Wrong Type or Price input")
                    else:
                        if order_type == 1:
                            self.delete_order(person, price, "BUY")
                        else:
                            self.delete_order(person, price, "SELL")
                else:
                    raise ValueError("Invalid Integer")

                trade = self.engine.balance_orders()

                if trade:
                    self.accounting.balance_player_orders(trade)

                print("\n ----- \n")
                print(self.engine)
                print(self.accounting)
                print("\n ----- \n")

            self.stats()

            print("Ending Round\n\n\n")
            self.engine.wipe()
        print("End Game.\n\n\n")
        self.accounting.scoring(self.middle)


def simulate_game():
    """Function to start the game"""
    game = FixItGame()
    try:
        num_players = int(input("How many players are there?\t"))
    except:
        raise ValueError("Invalid number of players")
    else:
        players = [x for x in list(range(1, int(num_players) + 1))]
        game.set_up_game(players)

    start = input("Start game? (y) \t")
    if start == "y":
        game.play()
    else:
        print("No game.")


if __name__ == "__main__":
    simulate_game()
