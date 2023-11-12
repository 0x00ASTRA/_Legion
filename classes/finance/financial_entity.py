# src/finance/financial_entity.py
class FinancialEntity:
    def __init__(self, name: str, description: str='A financial entity'):
        self.name = name
        self.description = description