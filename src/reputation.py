from typing import Dict
import json

class Reputation:
    def __init__(self):
        self.keypairs: Dict[str, Dict] = {
            'total': {'points': 0},
            'hacking': {'points': 0},
            'company': {'points': 0},
            'darknet': {'points': 0},
            'clearnet': {'points': 0},
            'commerce': {'points': 0},
            'organization': {'name': '', 'points': 0}
        }

    def increment_reputation(self, key: str, target: str, points: float) -> None:
        if key in self.keypairs:
            if target not in self.keypairs[key]:
                self.keypairs[key][target] = {'points': 0}
            self.keypairs[key][target]['points'] += points

    def decrement_reputation(self, key: str, target: str, points: float) -> None:
        if key in self.keypairs and target in self.keypairs[key]:
            self.keypairs[key][target]['points'] -= points

    def get_reputation(self, key: str, target: str) -> float:
        return self.keypairs.get(key, {}).get(target, {}).get('points', 0)

    def to_json(self) -> str:
        return json.dumps(self.keypairs)
