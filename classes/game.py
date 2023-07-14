import json

class Game:
    def __init__(self, character, tor_network, dark_web_marketplace, crypto_market):
        self.character = character
        self.tor_network = tor_network
        self.dark_web_marketplace = dark_web_marketplace
        self.crypto_market = crypto_market
        self.state = {}

    def start_new_game(self):
        # Initialize the game state
        self.state = {"character": self.character.to_json(), "tor_network": [str(node.id) for node in self.tor_network.nodes], 
                      "dark_web_marketplace": self.dark_web_marketplace.items, "crypto_market": self.crypto_market.prices}

    def save_game(self, filename):
        # Convert the game state to JSON and save it to a file
        with open(filename, 'w') as f:
            json.dump(self.state, f)

    def load_game(self, filename):
        # Load the game state from a file and convert it from JSON
        with open(filename, 'r') as f:
            self.state = json.load(f)
