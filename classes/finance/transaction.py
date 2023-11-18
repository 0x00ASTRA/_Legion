class Transaction:
    def __init__(
            self, tx_id: str, # Transaction ID
            amount: float, # Value of the Transaction
            type: str, # sent or received
            timestamp: float, # Timestamp in seconds
            metadata: dict  # JSON object
        ):
        self.tx_id = tx_id
        self.amount = amount
        assert(type.lower() in ["sent", "received", "deposit", "withdrawal"], "Error: Invalid must be 'sent' or 'received' / 'deposit' or 'withdrawal'")
        self.type = type.lower()
        self.timestamp = timestamp
        self.metadata = metadata