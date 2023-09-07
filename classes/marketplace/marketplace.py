from typing import List
from marketplace_item import MarketplaceItem

class Marketplace:
    def __init__(self, name: str, description: str, items: List[MarketplaceItem] = []):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item: MarketplaceItem, quantity: int) -> None:
        existing_item = next((i for i in self.items if i.uuid == item.uuid), None)
        if existing_item is None:
            item.quantity = quantity
            self.items.append(item)
        else:
            existing_item.quantity += quantity