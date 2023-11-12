from classes.marketplace.marketplace_item import MarketplaceItem
from classes.wallet.crypto_wallet import CryptoWallet
from classes.marketplace.cart import Cart
from classes.character.entity import Entity
from typing import List
from uuid import uuid4
import time

class Marketplace(Entity):
    def __init__(self, name: str, description: str, items: List[MarketplaceItem] = []):
        super().__init__(name=name)
        self.uuid = uuid4()
        self.description = description
        self.items = items
        self.wallet: CryptoWallet = CryptoWallet()
        self.bank: CryptoWallet = CryptoWallet()

    def add_item(self, item: MarketplaceItem, quantity: int) -> bool, str:

        try:
            existing_item = next((i for i in self.items if i.uuid == item.uuid), None)
            if existing_item is None:
                item.quantity = quantity
                self.items.append(item)
                return True, "Success: Item added to marketplace"
            else:
                existing_item.quantity += quantity
                return True, "Success: Item quantity increased"

        except:

            return False, "Error: Unable to add item to marketplace"
    
    async def checkout(self, cart: Cart, character: Character, payment_method: str) -> bool, str:
        # create reciept
        r = Reciept(merchant=self, tx_id=uuid4(), cart=cart, customer=character)
        # sign reciept
        r = self._sign_reciept(r)

        # wait for reciept to be signed by customer
        while not r.signed:
            signed_reciept = await character.sign_reciept(reciept=r, merchant=self.uuid, passkey=self.passkeys[character], public_key=character.keys[0])
            if signed_reciept.signed:
                r = signed_reciept
                break
            else:
                continue

        # remove items from inventory
        for item, qty in cart.items.items():
            self.remove_item(item, qty)

        


    def verify_item_exists(self, item: MarketplaceItem) -> bool:
        if not item in self.items:
            return False

        return True

    def get_item_qty(self, item: MarketplaceItem) -> int:
        for mp_item in self.items:
            if item.uuid == mp_item.uuid:
                return mp_item.quantity

        return 0
    
    def _sign_reciept(self, reciept: Reciept) -> bool, str:
        self._sign(reciept)
    
    async def _customer_sign_reciept(self, unsigned_reciept: Reciept, customer: Character) -> Reciept:
        public_key, _ = self.keys
        signed_reciept = await customer.sign_reciept(reciept=unsigned_reciept, merchant=self.uuid, passkey=self.passkeys[customer], public_key=public_key) )
        return signed_reciept

    def _transact(self, signed_reciept: Reciept, customer: Character, payment_method: str) -> bool, str:
        try:
            # check if the reciept is signed
            if not r.signed:
                return False, "Error: Reciept is not signed"

            # check if the customer has enough money
            # TO DO: use the network to check if the customer has enough money
            elif r.total > customer.get_balance(payment_method):
                return False, "Error: Customer does not have enough money"

            else:
                # deduct the money from the customer
                # TO DO: use the network to transact
                customer.deduct_balance(r.total, payment_method, self.public_key, self.passkeys[customer], r)
                return True, f"Success: Transaction successful | [TX ID]: {}"
        
        except:
            return False, "Error: Unable to transact"

    def update_item_price(self, item_index: int, price: float) -> bool:
        self.items[item_index].price = price

        return self.items[item_index].price == price