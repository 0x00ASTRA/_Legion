import uuid
import time

UUID  = uuid.uuid4

class Reciept:
    def __init__(
        self,
        merchant: Marketplace,
        tx_id: str,
        cart: Cart,
        customer: Character,
        merchant_fee: float | ServiceReciept = 0.0, # percentage or service reciept
    ):
        self.merchant = merchant
        self.tx_id = tx_id
        self.items = cart.items
        self.customer = customer
        self.timestamp = time.time()
        self.signed = False, False
        if type(merchant_fee) == float:
            self.merchant_fee = self.merchant_fee
        
        elif type(merchant_fee) == ServiceReciept:
            self.service_reciept = merchant_fee
            self.merchant_fee = merchant_fee.total
        
        else:
            raise TypeError("Merchant fee must be a float (percentage  of total) or ServiceReciept")

        self.total = self._calculate_total()

    def _calculate_total(self) -> float:
        total = 0
        for item, qty in self.items.items():
            total += item.price * qty
        
        total += self.merchant_fee
        return total

    def merchant_sign(self, merchant: Marketplace) -> bool:
        signature = merchant._sign_reciept(self)
        if signature:
            self.signed = True
            return True

        else:
            return False

    def customer_sign(self, customer: Character) -> bool:
        signature = customer._sign_reciept(self)
        if signature:
            self.signed = , True
            return True

    def to_json(self) -> Dict[str, str]:
        return {
            "merchant": str(self.merchant.uuid),
            "customer": str(self.customer.uuid),
            "tx_id": str(self.tx_id),
            "items": str(self.items),
            "merchant_fee": str(self.merchant_fee),
            "total": str(self.total),
            "timestamp": str(self.timestamp),
        }

        
            