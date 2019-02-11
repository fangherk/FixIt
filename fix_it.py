import random
from collections import deque, namedtuple

class FixItGame:
    def __init__(self):
        self.deck = deque(list(range(1,14))*4)
        self.rounds = 3
        self.middle = []
        self.accounting = {}

    def set_up_game(self, players):
        print("Shuffling Deck of {} cards".format(len(self.deck)))
        random.shuffle(self.deck)

        print("Draw Three Cards and put them in the middle")
        for _ in range(self.rounds):
            self.middle.append(self.deck.pop())

        print("Adding players to game")

        for name in players:
            draw_card = self.deck.pop()
            self.accounting[name] = Player(name, draw_card)

        print(self.stats())
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
        print("Player {} wins", winner.name)

    def play(self):
        num_cards = len(self.accounting) + self.rounds
        for turn in range(1, self.rounds+1):
            print("Total Cards in Play {}".format(num_cards))
            print("Revealing Cards: {}\n".format(self.middle[:turn]))
            while True:
                buyer = input("Press O to end turn. Who would like to buy?\n")
                if buyer == "O":
                    break
                seller = input("What is the seller id?\n")
                price = input("What is the price of the share?\n")

                Score = namedtuple("Score", "pot_value num_shares party")
                self.accounting[int(buyer)].add_trade(Score(int(price), -1, seller))
                self.accounting[int(seller)].add_trade(Score(int(price), 1, buyer))

            self.stats()
            print("Ending Round\n\n\n")
            print("End Game.\n\n\n")
            self.scoring()

class Player():
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.history = []

    def add_trade(self, trade):
        self.history.append(trade)

    def __str__(self):
        return "Player {} History: {} ".format(str(self.name),str(self.history))

def simulate_game():
    game = FixItGame()
    players = [1,2,3]
    game.set_up_game(players)
    game.play()

if __name__ == "__main__":
    simulate_game()
