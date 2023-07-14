class Reputation:
    def __init__(self):
        self.reputation_points = 0

    def increment_reputation(self, points):
        self.reputation_points += points

    def decrement_reputation(self, points):
        self.reputation_points -= points

    def get_reputation(self):
        return self.reputation_points

    def to_json(self):
        return self.reputation_points