from typing import List
from .marketplace_item import MarketplaceItem
from .marketplace import Marketplace

class DarkwebMarketplace(Marketplace):
    def __init__(self, name: str, description: str, items: List[MarketplaceItem] = ...):
        super().__init__(name, description, items)
