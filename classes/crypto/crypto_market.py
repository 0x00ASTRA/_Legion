import random
import classes.crypto.crypto_currency as CryptoCurrency

class CryptoMarket:
    def __init__(self, prices):
        self.currencies: CryptoCurrency = []

    def update_prices(self):
        for currency in self.prices:
            # The price of each currency fluctuates randomly to simulate demand and supply
            self.currencies[currency].price *= random.uniform(0.9, 1.1)
