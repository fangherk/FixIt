from collections import namedtuple


class AccountingBook:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        """Add player to list of players"""
        self.players[player.name] = player

    def balance_player_orders(self, trade):
        """Adds trade to each relevant player's history"""

        Score = namedtuple("Score", "pot_value num_shares party")
        print(trade)
        self.players[trade.buyer].add_trade(
            Score(trade.score, 1, trade.seller))
        self.players[trade.seller].add_trade(
            Score(trade.score, -1, trade.buyer))
        #Trade = namedtuple("Trade", "seller buyer score")
        # seller = self.players[trade.seller]
        # buyer = self.players[trade.buyer]
        # for i in range(len(seller.offers)):
        #     order = seller.offers[i]
        #     if order.price == trade.score:
        #         seller.offers.pop(i)
        #         break
        # for i in range(len(buyer.offers)):
        #     order = buyer.offers[i]
        #     if order.price == trade.score:
        #         buyer.offers.pop(i)
        #         break

    def scoring(self, middle):
        """Gives the winner player and shows profits made by all players"""
        player_cards = 0
        winner, winner_profit = None, None
        for player_id, player in self.players.items():
            player_cards += player.card
            total_value = sum(middle) + player_cards

        for player_id, player in self.players.items():
            history = player.history
            # Calculate pot value
            total_amount, total_shares = 0, 0
            for trade in history:
                amount, num_shares, _ = trade
                total_amount += amount * num_shares
                total_shares += num_shares

            profit = -(total_amount + (-1 * total_shares) * total_value)
            print("Player {} profits {}".format(player_id, profit))

            if not winner or not winner_profit:
                winner, winner_profit = player, profit
            if profit > winner_profit:
                winner = player
                winner_profit = profit

        print("Fair Value: {}".format(total_value))
        print("Player {} wins".format(winner.name))
        return winner.name

    def __repr__(self):
        """Show all players and their trades in a table"""
        num_players = len(self.players)
        out = num_players * " ───── "
        out = out + "\n"
        max_orders = max(
            [len(player.history) for player in self.players.values()])

        for i in range(max_orders + 2):
            for player_id, player in self.players.items():
                if i == 0:
                    out = out + "   {}   ".format(player_id)
                elif i == 1:
                    out = out + " ───── "
                else:
                    if (i - 2) < len(player.history):
                        trade = player.history[i - 2]
                        trade_value = trade.pot_value * trade.num_shares * (-1)
                        trade_value_str = str(trade_value)
                        if trade_value > 0:
                            trade_value_str = "+" + trade_value_str
                        out = out + "  {}  ".format(trade_value_str)
                    else:
                        out = out + "       "

            out = out + "\n"

        return out

    def __str__(self):
        return self.__repr__()
