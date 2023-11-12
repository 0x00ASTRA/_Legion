class Transaction:
    def __init__(self, tx_id: str, amount: float, debit_or_credit: str, timestamp: float, metadata: dict):
        self.tx_id = tx_id
        self.amount = amount
        assert(lower(debit_or_credit) in ["debit", "credit"], "Error: Invalid must be 'debit' or 'credit'")
        self.debit_or_credit = lower(debit_or_credit)
        self.timestamp = timestamp
        self.metadata = metadata