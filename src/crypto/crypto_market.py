import random
from typing import List
from src.crypto.crypto_currency import CryptoCurrency

class CryptoMarket:
    def __init__(self, prices):
        self.currencies: List[CryptoCurrency] = []

    def update_prices(self):
        for currency in self.prices:
            # The price of each currency fluctuates randomly to simulate demand and supply
            self.currencies[currency].price *= random.uniform(0.9, 1.1)
