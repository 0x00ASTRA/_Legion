from uuid import uuid4
from abc import ABC

class Currency(ABC):
    def __init__(self, name: str):
        self.name = name
        self.uuid = uuid4()
        self.supply: int =  0
    
    def get_name(self):
        return self.name
    
    def get_uuid(self):
        return self.uuid
    
    def get_supply(self):
        return self.supply
    
    def _mint(self, amount: int) -> tuple[bool, str]:
        try:
            self.supply += amount
            return True, f"Success: {amount} {self.name} Minted"
        except:
            return False, "Error: Unable to mint"
        
    def _burn(self, amount: int) -> tuple[bool, str]:
        try:
            self.supply -= amount
            return True, f"Success: {amount} {self.name} Burned"
        except:
            return False, "Error: Unable to burn"
    
        