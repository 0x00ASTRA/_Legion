# Import classes from their respective modules
from classes.character import Character, Reputation, LevelingSystem
from classes.attacks import Virus, Ransomware, Worm, Phishing, Exploit
from classes.computer import Computer
from classes.hardware.hardware import CPU, GPU, RAM, Storage
from classes.network.network import Node, Network
from classes.crypto.crypto_currency import CryptoWallet
from classes.marketplace import DarkWebMarketplace
from classes.game import Game
from classes.crypto.crypto_market import CryptoMarket

# Create a character with a Tor network and a crypto wallet
tor_network = TorNetwork()
node = Node()
tor_network.add_node(node)
wallet = CryptoWallet(currencies={"BTC": 1, "ETH": 2})
character = Character(name="Alice", skills={"hacking": 5}, money=10000, reputation=Reputation(), level=LevelingSystem(xp_to_level_up=100), tor_network=tor_network, wallet=wallet)

# Create a dark web marketplace and a crypto market
dark_web_marketplace = DarkWebMarketplace(items={"illegal software": 0.5, "stolen credit card": 0.2, "hacker toolkit": 1})
crypto_market = CryptoMarket(prices={"BTC": 50000, "ETH": 2000})

# Create a game, start a new game, save the game state, and load the game state
game = Game(character, tor_network, dark_web_marketplace, crypto_market)
game.start_new_game()
game.save_game('game_state.json')
game.load_game('game_state.json')
