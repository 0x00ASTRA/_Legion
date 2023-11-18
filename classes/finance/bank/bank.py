from classes.finance.financial_entity import FinancialEntity
from classes.finance.bank.bank_account import BankAccount
from classes.finance.cash.cash_storage import CashStorage
from classes.finance.cash.cash import Cash
from classes.character.entity import Entity
from typing import List, Dict, Optional

# Abstract class
class Bank(FinancialEntity):
    def __init__(self, name: str, standard_cash: Cash, description: str = 'A bank', owners: List[Entity] = []):
        super().__init__(name, description)
        self.standard_cash = standard_cash
        self.owners = owners
        self.balance: float = 0
        self.accounts: Dict[str, List[BankAccount]] = {} # key: owner, value: list of accounts
        self.vault: CashStorage = CashStorage(name="Main Vault")
        self.members: List[Entity] = []

    def withdraw_cash(self, amount: float, deposit_location: CashStorage, cash: Optional[Cash] = None):
        if cash is not None:
            return self.vault.retrieve(cash, amount, deposit_location)
        else:
            return self.vault.retrieve(self.standard_cash, amount, deposit_location)

    def get_deposit_location(self):
        return self.vault
    
    def deposit_cash(self, cash: Cash, amount: int):
        self.vault.store(cash, amount)

    def get_vault(self) -> CashStorage:
        return self.vault
    
    def get_owners(self) -> List[Entity]:
        return self.owners
    
    def get_accounts(self) -> Dict[str, List[BankAccount]]:
        return self.accounts
    
    def get_balance(self) -> float:
        return self.balance
    
    def get_vault_contents(self) -> Dict[Cash, int]:
        return self.vault.contents
    
    def get_standard_cash(self) -> Cash:
        return self.standard_cash
    
    def get_standard_cash_balance(self) -> int:
        return self.vault.contents[self.standard_cash]
    
    def _add_owner(self, owner: Entity):
        self.owners.append(owner)
    
    def _add_member(self, member: Entity):
        self.members.append(member)

    def _add_account(self, account: BankAccount):
        if account.owner.name in self.accounts:
            self.accounts[account.owner.name].append(account)
        else:
            self.accounts[account.owner.name] = [account]

    def _remove_account(self, account: BankAccount):
        account.balance = 0
        self.accounts[account.owner.name].remove(account)
    
    def _remove_owner(self, owner: Entity):
        self.owners.remove(owner)

    def _remove_member(self, member: Entity):
        self.members.remove(member)
        self.accounts[member.name] = []

    def open_account(self, owner: Entity) -> BankAccount:
        if owner.name in self.members:
            account = BankAccount(owner=owner, bank=self)
            self._add_account(account)
            return account
        
        else:
            self._add_member(owner)
            account = BankAccount(owner=owner, bank=self)
            self._add_account(account)
            return account
        
    def  close_account(self, account: BankAccount, deposit_location: CashStorage):
        self.withdraw_cash(account.get_balance(), deposit_location)
        self._remove_account(account)

    def close_membership(self, member: Entity):
        self._remove_member(member)