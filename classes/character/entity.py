from classes.utils import generate_keys
from uuid import uuid4
import rsa


class Entity:
    def __init__(self, name: str):
        self.name = name
        self.uuid = uuid4()
        self.keys = generate_keys()
        self.passkeys = {}

    def _sign(self, message: str) -> str:
        (pubkey, privkey) = self.keys
        signature = rsa.sign(message.encode(), privkey, 'SHA-256')
        return signature

    async def sign(self, message: str, passkey: str, public_key: str) -> tuple[bool, str]:
        try:
            if not public_key in self.passkeys:
                return False, "Error: Passkey does not exist"

            elif self.passkeys[public_key] != passkey:
                return False, "Error: Passkey does not match"

            signature = self._sign(message)
            return True, signature

        except:
            return False, "Error: Unable to sign message"

    def add_passkey(self, passkey: str, public_key: str, old_passkey: str =None) -> tuple[bool, str]:
        try:
            if old_passkey is not None:
                if not self.passkeys[public_key] == old_passkey:
                    return False, "Error [Unauthorized]: Passkey does not match"

            self.passkeys[public_key] = passkey
            return True, "Success: Passkey added"

        except:
            return False, "Error: Unable to add passkey"

    def remove_passkey(self, public_key: str, passkey: str) -> tuple[bool, str]:
        try:
            if not public_key in self.passkeys:
                return False, "Error: Passkey does not exist"
            
            elif self.passkeys[public_key] != passkey:
                return False, "Error [Unauthorized]: Passkey does not match"

            del self.passkeys[public_key]
            return True, "Success: Passkey removed"

        except:
            return False, "Error: Unable to remove passkey"

    def verify_passkey(self, passkey: str, public_key: str) -> tuple[bool, str]:
        try:
            if not public_key in self.passkeys:
                return False, "Error: Passkey does not exist"
            
            elif self.passkeys[public_key] != passkey:
                return False, "Error [Unauthorized]: Passkey does not match"
            
            return True, "Success"
        
        except:
            return False, "Error: Unable to verify passkey"
    