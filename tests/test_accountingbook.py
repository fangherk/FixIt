import unittest

import pytest
from fixit import AccountingBook, MatchingEngine, Order, Player


class TestAccountingBook:
    def setup(self):
        self.accounting = AccountingBook.AccountingBook()
        self.engine = MatchingEngine.MatchingEngine()

    def test_empty_book(self):
        """Test if accounting set of players is initialized to {}."""
        assert len(self.accounting.players) == 0

    def test_single_trade(self):
        """Test if single trade records into both parties' entries"""
        player1 = Player.Player("Joe", "3H")
        player2 = Player.Player("Jim", "3H")
        self.accounting.add_player(player1)
        self.accounting.add_player(player2)

        assert len(self.accounting.players) == 2

        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        order = Order.Order("Jim", 20)
        self.engine.add_order(order, "SELL")

        trade = self.engine.balance_orders()
        self.accounting.balance_player_orders(trade)

        assert len(self.accounting.players["Joe"].history) == 1
        assert len(self.accounting.players["Jim"].history) == 1

        assert (self.accounting.players["Joe"].history[0] == (20, 1, "Jim"))
        assert (self.accounting.players["Jim"].history[0] == (20, -1, "Joe"))

        assert self.accounting.scoring(["0H", "0H", "0H"]) == "Jim"

    def test_multiple_trades(self):
        """Test if making multiple transactions records into both parties' entries"""
        player1 = Player.Player("Joe", 3)
        player2 = Player.Player("Jim", 1)
        self.accounting.add_player(player1)
        self.accounting.add_player(player2)

        for _ in range(10):
            order = Order.Order("Joe", 20)
            self.engine.add_order(order, "BUY")

            order = Order.Order("Jim", 20)
            self.engine.add_order(order, "Sell")

            trade = self.engine.balance_orders()
            self.accounting.balance_player_orders(trade)

        assert len(self.accounting.players["Joe"].history) == 10
        assert len(self.accounting.players["Jim"].history) == 10

        assert self.accounting.scoring(["0H", "0H", "0H"]) == "Jim"
