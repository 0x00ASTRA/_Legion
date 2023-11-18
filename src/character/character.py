from typing import Dict, Any, Optional
from src.network.network import Network
from src.network.tor import TorNetwork
from src.character.entity import Entity
from src.finance.bank.bank_account import BankAccount
from src.finance.cash.cash_storage import CashStorage

class Character(Entity):
    def __init__(self,
                 name: str,
                 bank_accounts: Dict[str, BankAccount],
                 cash_storages: Dict[str, CashStorage],
                 skills: Dict[str, int], 
                 reputation: Dict[str, float],
                 level: int,
                 network: Optional[Network] = None,
                 tor_network: Optional[TorNetwork] = None
                ):
        super().__init__(name=name)
        self.bank_accounts = bank_accounts
        self.cash_storages = cash_storages
        self.skills = skills
        self.reputation = reputation
        self.level = level
        self.network = network
        self.tor_network = tor_network

    def to_json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "skills": self.skills,
            "reputation": self.reputation,
            "level": self.level,
            "network": self.network,
            "tor_network": self.tor_network
        }