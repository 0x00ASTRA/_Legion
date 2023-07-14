import random

class DarkWebMarketplace:
    def __init__(self, items):
        self.items = items  # Each item is represented as a string, and the value is the price in Bitcoin

    def buy(self, item, character):
        if item not in self.items:
            return "Item not found."
        if character.wallet.currencies["BTC"] < self.items[item]:
            return "Insufficient funds."
        character.wallet.currencies["BTC"] -= self.items[item]
        return f"You bought {item}."

    def update_prices(self):
        for item in self.items:
            # The price of each item fluctuates randomly to simulate demand and supply
            self.items[item] *= random.uniform(0.9, 1.1)
