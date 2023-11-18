from src.finance.currency import Currency

class Cash(Currency):
    def __init__(self, name: str):
        super().__init__(name)
    
    def print(self, amount: int):
        self._mint(amount)

    def burn(self, amount: int):
        self._burn(amount)