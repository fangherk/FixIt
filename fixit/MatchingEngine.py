import bisect
from collections import namedtuple


class Level:
    """Class to contain all orders of type that have a certain price"""

    def __init__(self, orders, price, time):
        self.orders = orders
        self.price = price
        self.time = time

    def __repr__(self):
        return "Orders:{}-Price:{}-Time:{}".format(self.orders, self.price,
                                                   self.time)

    def update_time(self):
        if self.orders:
            self.time = self.orders[0].time

    def __str__(self):
        return "Orders:{}-Price:{}-Time:{}".format(self.orders, self.price,
                                                   self.time)


class MatchingEngine:
    """Class to match orders made by players"""

    def __init__(self):
        self.bids = []
        self.offers = []

    def add_order(self, order, order_type="BUY"):
        """Add an order to the market"""
        book = self.bids if order_type == "BUY" else self.offers
        if not book or order.price > book[-1].price:
            new_level = Level([order], order.price, order.time)
            book.append(new_level)
        else:
            level_prices = [level.price for level in book]
            insert_index = bisect.bisect_left(level_prices, order.price)
            current_level = book[insert_index]
            if current_level.price == order.price:
                current_level.orders.append(order)
            else:
                new_level = Level([order], order.price, order.time)
                book.insert(insert_index, new_level)

    def clean_level(self):
        """Get rid of levels with no orders in them"""
        if self.bids:
            if not self.bids[-1].orders:
                self.bids.pop(-1)
        if self.offers:
            if not self.offers[0].orders:
                self.offers.pop(0)

    def delete_order(self, name, value, order_type="BUY"):
        """Delete an order in the market"""
        book = self.bids if order_type == "BUY" else self.offers
        level_prices = [level.price for level in book]
        price_index = bisect.bisect_left(level_prices, value)
        current_level = book[price_index]

        for i in range(len(current_level.orders)):
            order = current_level.orders[i]
            if order.name == name:
                current_level.orders.pop(i)
                break

        current_level.update_time()
        self.clean_level()

    def balance_orders(self):
        """Find out if a trade is completed and return the trade"""
        if not self.bids or not self.offers:
            return None

        highest_bid, lowest_offer = self.bids[-1], self.offers[0]
        Trade = namedtuple("Trade", "seller buyer score")
        trade = None
        ordering = None
        if lowest_offer.price <= highest_bid.price:
            bid_time, offer_time = highest_bid.time, lowest_offer.time
            num_offers, num_bids = len(highest_bid.orders), len(
                lowest_offer.orders)
            if bid_time < offer_time:
                order = lowest_offer.orders[0]
                trade_price = highest_bid.price
                num_orders = num_offers
                trans2, trans1 = lowest_offer, highest_bid
                ordering = "SELL"
            else:
                order = highest_bid.orders[0]
                trade_price = lowest_offer.price
                num_orders = num_bids
                trans2, trans1 = highest_bid, lowest_offer
                ordering = "BUY"

            count = 0
            while count < num_orders:
                # Same Level check.
                matching_order = trans1.orders[count]

                if order.name == matching_order.name:
                    count += 1
                    continue
                else:
                    trans1.orders.pop(count)
                    trans2.orders.pop(0)
                    trans1.update_time()
                    trans2.update_time()

                    if ordering == "SELL":
                        trade = Trade(order.name, matching_order.name,
                                      trade_price)
                    else:
                        trade = Trade(matching_order.name, order.name,
                                      trade_price)

                    print("Order matched {} sold {} bought @ {}".format(
                        trade.seller, trade.buyer, trade_price))

                    break
                count += 1

            self.clean_level()
            return trade

    def __repr__(self):
        return "Bids {}\nOffers {} ".format(str(self.bids), str(self.offers))

    def __str__(self):
        return "Bids {}\nOffers {} ".format(str(self.bids), str(self.offers))

    def wipe(self):
        """Set bids and offers to empty"""
        self.bids.clear()
        self.offers.clear()
