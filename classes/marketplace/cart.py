class Cart:
    def __init__(self, marketplace: Marketplace, customer: Character):
        self.customer = customer
        self.marketplace = marketplace
        self.items: Dict[MarketplaceItem, str] = {} # item => qty
        self.total: float = 0

    def add_item(self, item: MarketplaceItem, qty: int) -> bool, str:
        try:
            # check if the item exists
            if not self.marketplace.verify_item_exists(item):
                return False, "Error: Item does not exist"
        
            # check if the qty is available
            elif qty > self.marketplace.items[item]:
                return False, "Error: Quantity is not available"
            
            # add the item
            else:
                self.items[item] += qty
                self.total += (item.price * qty)
                return True, "Success: Item added to cart"

        except:
            return False, "Errror: Unable to add item to cart"

    
    def remove_item(self, item: MarketplaceItem, qty: int =0) -> bool, str:
        try:
            if qty == 0:
                del self.items[item]
                return True, "Success: Item removed from cart"

            else:
                self.items[item] -= qty
                self.total -= (item.price * qty)
                return True, "Success: Item quantity reduced"
        
        except:
            return False, "Error: Unable to remove item from cart"

    def delete_item(self, item: MarketplaceItem) -> bool, str:
        try:
            self.remove_item(item)
            return True, "Success: Item deleted"

        except:
            return False, "Error: Unable to delete item"

    def empty(self):
        try:
            self.items = {}
            self.total = 0
            return True, "Success: Cart emptied"
        
        except:
            return False, "Error: Unable to empty cart"