# ANSI escape codes for coloring
def color_red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def color_green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def color_yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"

def color_blue(text: str) -> str:
    return f"\033[94m{text}\033[0m"


from collections import defaultdict
from typing import List, Dict, Tuple
from time import sleep
from data import Bid, market_bids





# Displaying the expanded dictionary
# for minute, bids in market_bids.items():
#     print(f"Minute {minute}:")
#     for bid_type, bid_list in bids.items():
#         print(f"  {bid_type.capitalize()} Bids: {bid_list}")


class EnergyMarket:
    def __init__(self):
        self.buy_bids: Dict[str, List[Bid]] = defaultdict(list)
        self.sell_bids: Dict[str, List[Bid]] = defaultdict(list)

    def register_buy_bid(self, bid: Bid):
        self.buy_bids[bid.bidder_id].append(bid)

    def register_sell_bid(self, bid: Bid):
        self.sell_bids[bid.bidder_id].append(bid)

    # def match_bids(self) -> List[Tuple[Bid, Bid]]:
    #     matched_transactions = []
    #     for buy_bidder, buy_bid_list in list(self.buy_bids.items()):
    #         for buy_bid in buy_bid_list[:]:  # iterate over a copy of the list
    #             for sell_bidder, sell_bid_list in list(self.sell_bids.items()):
    #                 for sell_bid in sell_bid_list[:]:  # iterate over a copy of the list
    #                     if buy_bid.price >= sell_bid.price and buy_bid.amount == sell_bid.amount:
    #                         matched_transactions.append((buy_bid, sell_bid))
    #                         sell_bid_list.remove(sell_bid)
    #                         buy_bid_list.remove(buy_bid)
    #                         break
    #                 if buy_bid not in buy_bid_list:
    #                     break  # break if the buy bid was matched and removed

    #     # Remove empty lists from the dictionaries
    #     self.buy_bids = {bidder: bids for bidder, bids in self.buy_bids.items() if bids}
    #     self.sell_bids = {bidder: bids for bidder, bids in self.sell_bids.items() if bids}

    #     return matched_transactions

    def match_bids(self) -> List[Tuple[Bid, Bid]]:
        matched_transactions = []

        # Sort buy bids in descending order of price and sell bids in ascending order
        sorted_buy_bids = sorted((bid for bids in self.buy_bids.values() for bid in bids), 
                                 key=lambda x: (-x.price, x.amount))
        sorted_sell_bids = sorted((bid for bids in self.sell_bids.values() for bid in bids), 
                                  key=lambda x: (x.price, x.amount))

        buy_index, sell_index = 0, 0

        while buy_index < len(sorted_buy_bids) and sell_index < len(sorted_sell_bids):
            buy_bid = sorted_buy_bids[buy_index]
            sell_bid = sorted_sell_bids[sell_index]

            if buy_bid.price >= sell_bid.price:
                transaction_amount = min(buy_bid.amount, sell_bid.amount)

                if transaction_amount > 0:
                    # Record the transaction before reducing the bid amounts
                    matched_transactions.append((buy_bid, sell_bid, transaction_amount))

                    # Update the amounts of the bids
                    buy_bid.amount -= transaction_amount
                    sell_bid.amount -= transaction_amount

                if buy_bid.amount == 0:
                    buy_index += 1
                if sell_bid.amount == 0:
                    sell_index += 1
            else:
                buy_index += 1

        self.buy_bids = {bidder: [bid for bid in bids if bid.amount > 0] 
                         for bidder, bids in self.buy_bids.items()}
        self.sell_bids = {bidder: [bid for bid in bids if bid.amount > 0] 
                          for bidder, bids in self.sell_bids.items()}

        # Print out the matched transactions
        print("Matched Transactions:")
        for buy, sell, amount in matched_transactions:
            # print(f"{sell.bidder_id} sold to {buy.bidder_id} - {amount} units at {buy.price} price")
            print(f"{color_red(sell.bidder_id)} sold to {color_green(buy.bidder_id)} - {amount} units at {buy.price} price")
            sleep(1)

        return matched_transactions


    def display_bids(self):
        print(color_yellow("Buy Bids:"))
        for bids in self.buy_bids.values():
            for bid in bids:
                print(color_green(f"Bidder: {bid.bidder_id}, Amount: {bid.amount}, Price: {bid.price}"))
        
        print(color_yellow("\nSell Bids:"))
        for bids in self.sell_bids.values():
            for bid in bids:
                # print(color_red(f"Bidder: {bid.bidder_id}, Amount: {bid.amount}, Price: {bid.price}"))
                # print(f"{color_red(sell.bidder_id)} sold to {color_green(bid.bidder_id)} - {bid.amount} units at {bid.price} price")
                sleep(1)

# Create an instance of the market
market = EnergyMarket()

# Iterate through the market_bids dictionary and register bids
for minute, bids in market_bids.items():
    for buy_bid in bids['buy']:
        market.register_buy_bid(buy_bid)
    for sell_bid in bids['sell']:
        market.register_sell_bid(sell_bid)

# Now you can process and display the bids
matched_transactions = market.match_bids()
# print("Matched Transactions:")
# for buy, sell in matched_transactions:
#      print("Matched Transactions:")
#      print(f"{sell.bidder_id} sold to {buy.bidder_id} - {buy.amount} units at {buy.price} price")
#      sleep(1)

    # print(f"Buyer: {buy.bidder_id} and Seller: {sell.bidder_id} for {buy.amount} units at {buy.price} price")

# market.display_bids()