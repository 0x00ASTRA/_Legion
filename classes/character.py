class Character:
    def __init__(self, name, skills, money, reputation, level, tor_network, wallet):
        self.name = name
        self.skills = skills
        self.money = money
        self.reputation = reputation
        self.level = level
        self.tor_network = tor_network
        self.wallet = wallet

    def to_json(self):
        return {"name": self.name, "skills": self.skills, "money": self.money, 
                "reputation": self.reputation.to_json(), "level": self.level, 
                "wallet": self.wallet.currencies}
