import random

class CryptoCurrency:
    def __init__(self, name, symbol, initial_price):
        self.name = name
        self.symbol = symbol
        self.price = initial_price

    def update_price(self):
        # The price of the currency fluctuates randomly to simulate demand and supply
        self.price *= random.uniform(0.9, 1.1)

    def to_json(self):
        return {"name": self.name, "symbol": self.symbol, "price": self.price}
