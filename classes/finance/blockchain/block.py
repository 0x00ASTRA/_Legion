from classes.finance.blockchain.consensus.consensus import Consensus
from typing import Optional
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils


class Block:
    def __init__(self, timestamp: float, data: str, previous_hash: str, hash: str, nonce: int = 0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash
        self.signature: Optional[str] = None
        self.nonce = nonce  # Nonce for proof-of-work

    def mine(self, consensus: Consensus) -> None:
        """
        Mines the block using the provided consensus mechanism.
        """
        consensus.mine_block(self)

    def view(self) -> str:
        """
        Returns a string representation of the block's data.
        """
        return str(self.data)

    def sign(self, private_key: bytes) -> None:
        """
        Signs the block with a given private key.
        """
        if not self.signature:
            block_string = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
            signature = sign_message(block_string.encode(), private_key)
            self.signature = signature.hex()

    def calculate_hash(self) -> str:
        """
        Calculates and returns the hash of the block.
        """
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}{self.signature}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def sign_message(message: bytes, private_key: bytes) -> bytes:
    """
    Sign a message using ECDSA.
    """
    private_key = serialization.load_der_private_key(private_key, password=None, backend=default_backend())
    signature = private_key.sign(message, ec.ECDSA(utils.Prehashed(utils.Prehashed.SHA256())))
    return signature
