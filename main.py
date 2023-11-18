# Import classes from their respective modules
from src.character import Character
from src.reputation import Reputation
from src.attacks import Virus, Ransomware, Worm, Phishing, Exploit
from src.computer import Computer
from src.hardware import CPU, GPU, RAM, Storage
from src.network.network import Router
from src.network.tor import TorNetwork
from src.crypto.crypto_wallet import CryptoWallet
from src.marketplace import DarkWebMarketplace
from src.game import Game
from src.crypto.crypto_market import CryptoMarket

# Create a character with a Tor network and a crypto wallet
tor_network = TorNetwork()
node = Router()
tor_network.add_node(node)
wallet = CryptoWallet(currencies={"BTC": 1, "ETH": 2})
character = Character(name="Alice", skills={"hacking": 5}, money=10000, reputation=Reputation(), level=0, tor_network=tor_network, wallet=wallet)
players_PC = Computer(CPU("Intel", "Core i7", 3.5), GPU("NVIDIA", "RTX 3060", 12, 2.5), RAM(16), Storage("SSD", 500, 1000))
# Create a dark web marketplace and a crypto market
dark_web_marketplace = DarkWebMarketplace(items={"illegal software": 0.5, "stolen credit card": 0.2, "hacker toolkit": 1})
crypto_market = CryptoMarket(prices={"BTC": 50000, "ETH": 2000})

# Create a game, start a new game, save the game state, and load the game state
game = Game(character, tor_network, dark_web_marketplace, crypto_market)
game.start_new_game()
game.save_game('game_state.json')
game.load_game('game_state.json')
