import uuid

class MarketplaceItem:
    def __init__(self, name: str, price: float, category: str, description: str ='', quantity: int = 0):
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.uuid = uuid.uuid4()
        self.quantity = quantity
