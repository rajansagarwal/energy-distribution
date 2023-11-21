from collections import defaultdict
from typing import List, Dict, Tuple
from time import sleep
# Create the dictionary with more example data
# Define the Bid class
class Bid:
    def __init__(self, bidder_id: str, amount: int, price: float):
        self.bidder_id = bidder_id
        self.amount = amount
        self.price = price

    def __repr__(self) -> str:
        return f"Bidder: {self.bidder_id}, Amount: {self.amount}, Price: {self.price}"


market_bids: Dict[int, Dict[str, List[Bid]]] = {
    1: {
        'buy': [Bid("Buyer1A", 100, 10), Bid("Buyer1B", 120, 9.5), Bid("Buyer1C", 90, 10.5)],
        'sell': [Bid("Seller1A", 50, 12), Bid("Seller1B", 60, 11.5), Bid("Seller1C", 70, 11)]
    },
    2: {
        'buy': [Bid("Buyer2A", 150, 11), Bid("Buyer2B", 160, 10.5), Bid("Buyer2C", 140, 11.5)],
        'sell': [Bid("Seller2A", 60, 13), Bid("Seller2B", 65, 12.5), Bid("Seller2C", 55, 13.5)]
    },
    3: {
        'buy': [Bid("Buyer3A", 200, 10.2), Bid("Buyer3B", 180, 10), Bid("Buyer3C", 190, 10.3)],
        'sell': [Bid("Seller3A", 80, 11), Bid("Seller3B", 85, 11.2), Bid("Seller3C", 75, 10.8)]
    },
    4: {
        'buy': [Bid("Buyer4A", 100, 9), Bid("Buyer4B", 110, 9.3), Bid("Buyer4C", 105, 9.1)],
        'sell': [Bid("Seller4A", 50, 10), Bid("Seller4B", 55, 9.8), Bid("Seller4C", 45, 10.2)]
    },
    5: {
        'buy': [Bid("Buyer5A", 250, 8.5), Bid("Buyer5B", 240, 8.7), Bid("Buyer5C", 230, 8.9)],
        'sell': [Bid("Seller5A", 100, 9), Bid("Seller5B", 95, 9.2), Bid("Seller5C", 90, 9.5)]
    },
    6: {
        'buy': [Bid("Buyer6A", 260, 8.3), Bid("Buyer6B", 250, 8.5), Bid("Buyer6C", 240, 8.7)],
        'sell': [Bid("Seller6A", 110, 8.9), Bid("Seller6B", 105, 9.1), Bid("Seller6C", 100, 9.3)]
    },
    7: {
        'buy': [Bid("Buyer7A", 270, 8.1), Bid("Buyer7B", 260, 8.3), Bid("Buyer7C", 250, 8.5)],
        'sell': [Bid("Seller7A", 120, 8.7), Bid("Seller7B", 115, 8.9), Bid("Seller7C", 110, 9.1)]
    },
    8: {
        'buy': [Bid("Buyer8A", 280, 7.9), Bid("Buyer8B", 270, 8.1), Bid("Buyer8C", 260, 8.3)],
        'sell': [Bid("Seller8A", 130, 8.5), Bid("Seller8B", 125, 8.7), Bid("Seller8C", 120, 8.9)]
    },
    9: {
        'buy': [Bid("Buyer9A", 290, 7.7), Bid("Buyer9B", 280, 7.9), Bid("Buyer9C", 270, 8.1)],
        'sell': [Bid("Seller9A", 140, 8.3), Bid("Seller9B", 135, 8.5), Bid("Seller9C", 130, 8.7)]
    },
    10: {
        'buy': [Bid("Buyer10A", 300, 7.5), Bid("Buyer10B", 290, 7.7), Bid("Buyer10C", 280, 7.9)],
        'sell': [Bid("Seller10A", 150, 8.1), Bid("Seller10B", 145, 8.3), Bid("Seller10C", 140, 8.5)]
    },
        11: {
        'buy': [Bid("Buyer11A", 310, 7.3), Bid("Buyer11B", 300, 7.5), Bid("Buyer11C", 290, 7.7)],
        'sell': [Bid("Seller11A", 160, 7.9), Bid("Seller11B", 155, 8.1), Bid("Seller11C", 150, 8.3)]
    },
    12: {
        'buy': [Bid("Buyer12A", 320, 7.1), Bid("Buyer12B", 310, 7.3), Bid("Buyer12C", 300, 7.5)],
        'sell': [Bid("Seller12A", 170, 7.7), Bid("Seller12B", 165, 7.9), Bid("Seller12C", 160, 8.1)]
    },
    13: {
        'buy': [Bid("Buyer13A", 330, 6.9), Bid("Buyer13B", 320, 7.1), Bid("Buyer13C", 310, 7.3)],
        'sell': [Bid("Seller13A", 180, 7.5), Bid("Seller13B", 175, 7.7), Bid("Seller13C", 170, 7.9)]
    },
    14: {
        'buy': [Bid("Buyer14A", 340, 6.7), Bid("Buyer14B", 330, 6.9), Bid("Buyer14C", 320, 7.1)],
        'sell': [Bid("Seller14A", 190, 7.3), Bid("Seller14B", 185, 7.5), Bid("Seller14C", 180, 7.7)]
    },
    15: {
        'buy': [Bid("Buyer15A", 350, 6.5), Bid("Buyer15B", 340, 6.7), Bid("Buyer15C", 330, 6.9)],
        'sell': [Bid("Seller15A", 200, 7.1), Bid("Seller15B", 195, 7.3), Bid("Seller15C", 190, 7.5)]
    },
     16: {
        'buy': [Bid("Buyer16A", 360, 6.3), Bid("Buyer16B", 350, 6.5), Bid("Buyer16C", 340, 6.7)],
        'sell': [Bid("Seller16A", 210, 6.9), Bid("Seller16B", 205, 7.1), Bid("Seller16C", 200, 7.3)]
    },
    17: {
        'buy': [Bid("Buyer17A", 370, 6.1), Bid("Buyer17B", 360, 6.3), Bid("Buyer17C", 350, 6.5)],
        'sell': [Bid("Seller17A", 220, 6.7), Bid("Seller17B", 215, 6.9), Bid("Seller17C", 210, 7.1)]
    },
    18: {
        'buy': [Bid("Buyer18A", 380, 5.9), Bid("Buyer18B", 370, 6.1), Bid("Buyer18C", 360, 6.3)],
        'sell': [Bid("Seller18A", 230, 6.5), Bid("Seller18B", 225, 6.7), Bid("Seller18C", 220, 6.9)]
    },
    19: {
        'buy': [Bid("Buyer19A", 390, 5.7), Bid("Buyer19B", 380, 5.9), Bid("Buyer19C", 370, 6.1)],
        'sell': [Bid("Seller19A", 240, 6.3), Bid("Seller19B", 235, 6.5), Bid("Seller19C", 230, 6.7)]
    },
    20: {
        'buy': [Bid("Buyer20A", 400, 5.5), Bid("Buyer20B", 390, 5.7), Bid("Buyer20C", 380, 5.9)],
        'sell': [Bid("Seller20A", 250, 6.1), Bid("Seller20B", 245, 6.3), Bid("Seller20C", 240, 6.5)]
    }
}