from classes.crypto.crypto_currency import CryptoCurrency
class CryptoMarketItem:
    def __init__(self, name: str, description: str, category:str, price: float, currency: CryptoCurrency):
        self.name: str = name
        self.description: str = description
        self.category: str = category
        self.price: float = price
        self.currency: CryptoCurrency = currency

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "price": self.price,
            "currency": self.currency
        }