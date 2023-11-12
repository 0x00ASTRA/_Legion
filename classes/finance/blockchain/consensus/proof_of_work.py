from classes.finance.blockchain.consensus.consensus import Consensus
from classes.finance.blockchain.block import Block
import time

class ProofOfWork(Consensus):
    def __init__(self, difficulty: int, target_prefix: str):
        self.difficulty = difficulty
        self.target_prefix = target_prefix

    def mine_block(self, block: Block) -> None:
        """
        Mines the block with a proof-of-work mechanism.
        """
        target_prefix = self.target_prefix * self.difficulty
        while not block.hash.startswith(target_prefix):
            block.nonce += 1
            block.hash = block.calculate_hash()
            block.timestamp = time.time()
