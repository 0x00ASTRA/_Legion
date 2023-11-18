from abc import ABC, abstractmethod
from src.finance.blockchain.block import Block
import time


class Consensus(ABC):
    @abstractmethod
    def mine_block(self, block: Block) -> None:
        pass