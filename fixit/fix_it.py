import random
from collections import deque, namedtuple

from Order import Order
from MatchingEngine import MatchingEngine
from Player import Player

class FixItGame:
    def __init__(self):
        self.deck = deque(list(range(1,14))*4)
        self.rounds = 3
        self.middle = []
        self.engine = MatchingEngine()
        self.accounting = {}

    def set_up_game(self, players):
        print("\n\nShuffling Deck of {} cards".format(len(self.deck)))
        random.shuffle(self.deck)

        print("Draw Three Cards and put them in the middle")
        for _ in range(self.rounds):
            self.middle.append(self.deck.pop())

        print("Adding players to game\n\n\n")

        for name in players:
            draw_card = self.deck.pop()
            self.accounting[name] = Player(name, draw_card)

        print("Displaying accounting book")
        self.stats()
        print("Set up complete\n\n\n\n")

    def stats(self):
        for _, val in self.accounting.items():
            print(val)

    def scoring(self):
        player_cards = 0
        winner, winner_profit = None, None
        for player_id, player in self.accounting.items():
            player_cards += player.card
            total_value = sum(self.middle) + player_cards

        for player_id, player in self.accounting.items():
            history = player.history
            # Calculate pot value
            total_amount, total_shares = 0, 0
            for trade in history:
                amount, num_shares, _ = trade
                total_amount += amount * num_shares
                total_shares += num_shares

            profit = total_amount + (-1*total_shares) * total_value
            print("Player {} profits {}".format(player_id, profit))

            if not winner or not winner_profit:
                winner, winner_profit = player, profit
            if profit > winner_profit:
                winner = player
                winner_profit = profit

        print("Fair Value: {}".format(total_value))
        print("Player {} wins".format(winner.name))

    def play(self):
        num_cards = len(self.accounting) + self.rounds
        for turn in range(1, self.rounds+1):
            print("Total Cards in Play {}".format(num_cards))
            print("Revealing Cards: {}\n".format(self.middle[:turn]))
            while True:
                buyer = input("Press 0 to end turn. Press 1 for buy. Press 2 for sell.\n")
                if buyer == "0":
                    break

                person = input("What is your id?\n")
                # ASSUME integer values
                price = input("What is the price of the share?\n")

                order = Order(person, int(price), 1)
                if buyer == "1":
                    self.engine.add_order(order, "BUY")
                if buyer == "2":
                    self.engine.add_order(order, "SELL")

                self.engine.balance_orders()
                print(self.engine)
                #Score = namedtuple("Score", "pot_value num_shares party")
                #self.accounting[int(buyer)].add_trade(Score(int(price), -1, seller))
                #self.accounting[int(seller)].add_trade(Score(int(price), 1, buyer))

            self.stats()
            print("Ending Round\n\n\n")
            self.engine.wipe()
        print("End Game.\n\n\n")
        self.scoring()

def simulate_game():
    game = FixItGame()
    num_players = input("How many players are there?\t")
    players = list(range(1, int(num_players)+1))
    game.set_up_game(players)

    start = input("Start game? (y) \t")
    if start == "y":
        game.play()
    else:
        print("No game.")

if __name__ == "__main__":
    simulate_game()
