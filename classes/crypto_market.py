import random

class CryptoMarket:
    def __init__(self, prices):
        self.prices = prices

    def update_prices(self):
        for currency in self.prices:
            # The price of each currency fluctuates randomly to simulate demand and supply
            self.prices[currency] *= random.uniform(0.9, 1.1)
