import unittest

from fixit import Order, MatchingEngine

class TestMatchingEngine(unittest.TestCase):

    def setUp(self):
        self.engine = MatchingEngine.MatchingEngine()

    def test_empty_engine(self):
        """ Check if an engine can be simply initialized"""
        self.assertEqual(self.engine.bids, [])
        self.assertEqual(self.engine.offers, [])

    def test_add_order(self):
        """ Add an order and check the results """
        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        level = self.engine.bids[0]
        order_result = level.orders[0]
        self.assertEqual(len(self.engine.bids), 1)
        self.assertEqual(len(level.orders), 1)
        self.assertEqual(level.price, 20)
        self.assertEqual(order_result.price, 20)
        self.assertEqual(order_result.name, "Joe")


    def test_match_simple_order(self):
        """ Match an order """

        order = Order.Order("Joe", 20)
        self.engine.add_order(order, "BUY")

        order = Order.Order("Jim", 20)
        self.engine.add_order(order, "SELL")

        self.assertEqual(len(self.engine.bids), 1)
        self.assertEqual(len(self.engine.offers), 1)

        self.engine.balance_orders()

        self.assertEqual(len(self.engine.bids), 0)
        self.assertEqual(len(self.engine.offers), 0)

    def test_make_many_same_orders(self):

        for _ in range(10):
            order = Order.Order("A", 20)
            self.engine.add_order(order, "BUY")

        #only 1 level
        self.assertEqual(len(self.engine.bids), 1)

        #check length bids = number orders made
        self.assertEqual(len(self.engine.bids[0].orders), 10)

        #time of level is equal to time of first order
        self.assertEqual(self.engine.bids[0].time, self.engine.bids[0].orders[0].time)
