from typing import Dict, Any
from .network.tor import TorNetwork

class Character:
    def __init__(self, name: str, skills: Dict[str, int], money: Dict[str, float], 
                 reputation: Dict[str, float], level: int, tor_network: TorNetwork, wallet: Dict[str, Any]):
        self.name = name
        self.skills = skills
        self.money = money
        self.reputation = reputation
        self.level = level
        self.tor_network = tor_network
        self.wallet = wallet

    def to_json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "skills": self.skills,
            "money": self.money, 
            "reputation": self.reputation,
            "level": self.level,
            "wallet": self.wallet
        }
