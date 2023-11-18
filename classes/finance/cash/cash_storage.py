from classes.finance.cash.cash import Cash
from typing import Dict

class CashStorage:
    def __init__(self, name: str):
        self.name = name
        self.contents: Dict[Cash, int] = {}

    def store(self, cash: Cash, amount: int):
        if cash not in self.contents:
            self.contents[cash] = 0
        
        self.contents[cash] += amount

    def retrieve(self, cash: Cash, amount: int, deposit_location: "CashStorage"):
        self.contents[cash] -= amount
        deposit_location.store(cash, amount)