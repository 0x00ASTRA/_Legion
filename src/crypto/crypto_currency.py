import random
import os
import json

class CryptoCurrency:
    def __init__(self, name, symbol, initial_price, initial_supply):
        self.name = name
        self.symbol = symbol
        self.price = initial_price
        self.total_supply = initial_supply

    def _mint(self, amount, reciever):
        self.total_supply += amount
        reciever.recieve_transaction(self, amount, self)

    def _burn(self, amount, account):
        self.total_supply -= amount
        account.currencies[self].balance -= amount


    def update_price(self):
        # The price of the currency fluctuates randomly to simulate demand and supply
        self.price *= random.uniform(0.9, 1.1)

    def to_json(self):
        return {
            "name": self.name,
            "symbol": self.symbol,
            "price": self.price
        }

    def from_json(self, file_path: str):
        # load the json config file
        file_name, file_ext = os.splitext(file_path)
        if not file_ext == '.json':
            print(f"Error: File extention not compatible '{file_ext}', expected '.json'")
        try:
            self.__dict__ = json.loads(file_path)
        except:
            raise(TypeError(f'Unable to load the json configuration: {file_path}'))