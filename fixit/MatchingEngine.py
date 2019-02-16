import bisect

class Level:
    def __init__(self, orders, price, time):
        self.orders = orders
        self.price = price
        self.time = time

    def __repr__(self):
        return "Orders:{}-Price:{}-Time:{}".format(self.orders,
                                                   self.price,
                                                   self.time)
    def update_time(self):
        if self.orders:
            self.time = self.orders[0].time

    def __str__(self):
        return "Orders:{}-Price:{}-Time:{}".format(self.orders,
                                                   self.price,
                                                   self.time)
class MatchingEngine:
    def __init__(self):
        self.bids = []
        self.offers = []

    def add_order(self, order, order_type="BUY"):
        book = self.bids if order_type == "BUY" else self.offers
        if not book:
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
        if len(self.bids[-1].orders) == 0:
            self.bids.pop(-1)
        if len(self.offers[0].orders) == 0:
            self.offers.pop(0)

    def balance_orders(self):
        if not self.bids or not self.offers:
            return

        highest_bid, lowest_offer = self.bids[-1], self.offers[0]

        if lowest_offer.price <= highest_bid.price:
            bid_time, offer_time = highest_bid.time, lowest_offer.time
            num_offers, num_bids = len(highest_bid.orders), len(lowest_offer.orders)
            if bid_time < offer_time:
                order = lowest_offer.orders[0]
                trade_price = highest_bid.price
                num_orders = num_offers
                trans2, trans1 = lowest_offer, highest_bid
            else:
                order = highest_bid.orders[0]
                trade_price = lowest_offer.price
                num_orders = num_bids
                trans2, trans1 = highest_bid, lowest_offer

            count = 0
            while count < num_orders:
                # Same Level check.
                matching_order = trans1.orders[count]
                if order.name == matching_order.name:
                    count +=1
                    continue
                else:
                    trans1.orders.pop(count)
                    trans2.orders.pop(0)
                    trans1.update_time()
                    trans2.update_time()

                    print("Order matched {} sold {} bought @ {}".format(order.name,
                                                                        matching_order.name,
                                                                        trade_price))
                count += 1

            self.clean_level()
            # TODO: Add a broadcast step. Accounting step here.

    def __repr__(self):
        return "Bids {}\nOffers {} ".format(str(self.bids),
                                            str(self.offers))

    def __str__(self):
        return "Bids {}\nOffers {} ".format(str(self.bids),
                                            str(self.offers))

    def wipe(self):
        self.bids.clear()
        self.offers.clear()
