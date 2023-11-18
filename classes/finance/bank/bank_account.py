from __future__ import annotations
from classes.finance.payment_account import PaymentAccount
from classes.character.entity import Entity
from classes.finance.transaction import Transaction
from classes.finance.cash.cash import Cash
from typing import List, Optional
from classes.utils import generate_keys
from classes.finance.cash.cash_storage import CashStorage
import uuid
import time

class BankAccount(PaymentAccount):
    def __init__(self, owner: Entity, bank: Bank):
        super().__init__(owner)
        self.balance: float = 0
        self.keys = generate_keys()
        self.public_key = self.keys[0]
        self.passkey = self.keys[1]
        self.bank = bank
        self.transactions: List[Transaction] = []

    def verify_passkey(self, passkey: str) -> bool:
        if self.owner.verify_passkey(passkey=passkey, public_key=self.public_key):
            return True
        else:
            return False
        
    def create_transaction(self, type: str, amount: float, metadata: {} = {}):
        tx_id = str(uuid.uuid4())
        transaction = Transaction(type=type, amount=amount, tx_id=tx_id, timestamp=int(time.time()), metadata=metadata)
        self.transactions.append(transaction)

    def withdraw(self, amount: float, deposit_location: CashStorage, cash: Optional[Cash] = None) -> tuple[bool, str]:
        # verify balance is sufficient
        if float(amount) > self.balance:
            return False, "Error: Insufficient funds"
    
        else:
            self.create_transaction('withdraw',amount)
            self.bank.withdraw_cash(amount, deposit_location=deposit_location, cash=cash)
            self.balance -= amount
            return True

    def deposit(self, cash: Cash, amount: float, cash_storage: CashStorage) -> tuple[bool, str]:
        bank_vault = self.bank.get_deposit_location()
        cash_storage.retrieve(cash, amount, bank_vault)
        self.balance += amount
        return True
    
    def get_balance(self) -> float:
        return self.balance