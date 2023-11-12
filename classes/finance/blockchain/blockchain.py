from classes.finance.financial_entity import FinancialEntity
from classes.finance.blockchain.block import Block
from classes.finance.blockchain.consensus.proof_of_work import ProofOfWork
from typing import List
import time

class UTXO:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Blockchain(FinancialEntity):
    def __init__(self, name: str, description: str = 'A blockchain'):
        super().__init__(name, description)
        self.chain: List[Block] = []
        self.difficulty = 4  # Initial difficulty level
        self.block_generation_interval = 10  # Target time in seconds between block generations
        self.mining_reward = 10  # Reward for miners (you can adjust the amount)
        self.utxo_set: List[UTXO] = []  # UTXO set for tracking balances

    def add_block(self, block: Block) -> None:
        """
        Adds a mined block to the blockchain.
        """
        if self.is_valid_block(block):
            self.adjust_difficulty()
            self.process_mining_reward(block)
            self.update_utxo_set(block)
            self.chain.append(block)
            print(f"Block added to {self.name}'s blockchain with difficulty {self.difficulty}.")
        else:
            print("Invalid block. Block not added.")

    def mine_block(self, miner_address: str) -> None:
        """
        Mines a new block with the provided data and adds it to the blockchain.
        """
        reward_transaction = {
            'from': 'system',
            'to': miner_address,
            'amount': self.mining_reward,
            'message': 'Mining reward',
        }

        new_block = Block(
            timestamp=time.time(),
            data=f"Reward: {self.mining_reward}",
            previous_hash=self.get_last_block_hash(),
            transactions=[reward_transaction],
        )

        proof_of_work = ProofOfWork(difficulty=self.difficulty)
        new_block.mine(proof_of_work)
        self.add_block(new_block)

    def process_mining_reward(self, block: Block) -> None:
        """
        Processes the mining reward for the miner.
        """
        miner_reward_transaction = block.transactions[0]
        miner_address = miner_reward_transaction['to']
        self.add_utxo(UTXO(miner_address, miner_reward_transaction['amount']))

    def update_utxo_set(self, block: Block) -> None:
        """
        Updates the UTXO set based on the transactions in the mined block.
        """
        for transaction in block.transactions:
            sender_address = transaction['from']
            recipient_address = transaction['to']
            amount = transaction['amount']

            # Remove spent UTXOs
            self.utxo_set = [utxo for utxo in self.utxo_set if utxo.address != sender_address]

            # Add new UTXOs for recipient and sender change
            if recipient_address != 'system':  # Exclude mining reward
                self.add_utxo(UTXO(recipient_address, amount))
            if transaction.get('change', 0) > 0:
                self.add_utxo(UTXO(sender_address, transaction['change']))

    def add_utxo(self, utxo: UTXO) -> None:
        """
        Adds a new UTXO to the UTXO set.
        """
        self.utxo_set.append(utxo)

    def get_balance(self, address: str) -> float:
        """
        Returns the balance of an address based on the UTXO set.
        """
        return sum(utxo.amount for utxo in self.utxo_set if utxo.address == address)

# Example usage
blockchain = Blockchain(name="MyBlockchain")
blockchain.mine_block(miner_address="Alice")
blockchain.mine_block(miner_address="Bob")

# Transfer some funds from Alice to Bob
blockchain.mine_block(miner_address="Alice")
blockchain.mine_block(miner_address="Bob")

# Check balances
print("Alice's balance:", blockchain.get_balance("Alice"))
print("Bob's balance:", blockchain.get_balance("Bob"))
