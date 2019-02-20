import pytest
from fixit import Order, MatchingEngine


class TestMatchingEngine:
    def setup(self):
        self.engine = MatchingEngine.MatchingEngine()

    def test_empty_engine(self):
        """ Check if an engine can be simply initialized"""
        assert self.engine.bids == []
        assert self.engine.offers == []

    def test_add_order(self):
        """ Add an order and check the results """
        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        level = self.engine.bids[0]
        order_result = level.orders[0]
        assert len(self.engine.bids) == 1
        assert len(level.orders) == 1
        assert level.price == 20
        assert order_result.price == 20
        assert order_result.name == "Joe"

    def test_match_simple_order(self):
        """ Match an order """
        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        order = Order.Order("Jim", 20)
        self.engine.add_order(order, "SELL")

        assert len(self.engine.bids) == 1
        assert len(self.engine.offers) == 1

        self.engine.balance_orders()

        assert len(self.engine.bids) == 0
        assert len(self.engine.offers) == 0

    def test_make_many_same_orders(self):
        """Test if many of the same order can be made by a single player"""
        for _ in range(10):
            order = Order.Order("A", 20)
            self.engine.add_order(order, "BUY")

        #only 1 level
        assert len(self.engine.bids) == 1

        #check length bids = number orders made
        assert len(self.engine.bids[0].orders) == 10

        #time of level is equal to time of first order
        assert self.engine.bids[0].time == self.engine.bids[0].orders[0].time

    def test_delete_an_order(self):
        """Test deletion of an order"""
        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        assert len(self.engine.bids) == 1

        self.engine.delete_order("Joe", 20, "BUY")

        assert len(self.engine.bids) == 0
