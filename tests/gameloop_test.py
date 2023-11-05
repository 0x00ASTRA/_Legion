from classes.game import Game
from classes.character import Character
from classes.network.tor import TorNetwork
from classes.marketplace.darkweb_marketplace import DarkwebMarketplace
from classes.marketplace.marketplace_item import MarketplaceItem
from classes.crypto.crypto_market import CryptoMarket

# Market items
coke = MarketplaceItem(name='Cocaine (1g)', description='Straight from Columbia. Keeps the night owls ready for anything', price=100, category='Narcotics', quantity=500)
mdma = MarketplaceItem(name='MDMA (1 pill)', description='Pure ecstasy for a night of happiness', price=40, category='Narcotics', quantity=300)
stolen_credit_cards = MarketplaceItem(name='Stolen Credit Cards', description='Freshly skimmed, high balance', price=200, category='Fraud', quantity=100)
zero_day_exploit = MarketplaceItem(name='Zero-Day Exploit', description='Unpatched vulnerabilities for various systems', price=5000, category='Hacking Tools', quantity=3)
fake_passports = MarketplaceItem(name='Fake Passports', description='High-quality, machine-readable', price=3000, category='Forged Documents', quantity=10)
luxury_watches = MarketplaceItem(name='Luxury Watches', description='Stolen but exquisite', price=1500, category='Stolen Goods', quantity=25)
malware = MarketplaceItem(name='Advanced Malware', description='Stealthy and highly effective', price=1000, category='Hacking Tools', quantity=50)
ransomware = MarketplaceItem(name='Ransomware Kit', description='Ready-to-deploy, highly effective', price=4000, category='Hacking Tools', quantity=10)
firearms = MarketplaceItem(name='Handguns', description='Untraceable and clean', price=800, category='Weapons', quantity=20)
hitman_services = MarketplaceItem(name='Hitman Services', description='Discreet and professional', price=20000, category='Services', quantity=1)

# Create DarkwebMarketplace instance with all items
dwmp = DarkwebMarketplace(name='S1lk R04D', description='Anything goes for the right price', items=[coke, mdma, stolen_credit_cards, zero_day_exploit, fake_passports, luxury_watches, malware, ransomware, firearms, hitman_services])

# Create Character instance
name = "AJ"
skills = {}
money = {'USD': 2**6}
reputation = {}
level = 0
tor_network = TorNetwork()
wallet = {'BTC': 1, 'ETH': 5, 'SOL': 4000}
character = Character(name=name, skills=skills, money=money, reputation=reputation, level=level, tor_network=tor_network, wallet=wallet)
crypto_market = CryptoMarket(prices={'BTC': 25000, 'ETH': 1500, 'SOL': 68})
# Create Game instance
game = Game(character=character, tor_network=tor_network, dark_web_marketplace=dwmp, crypto_market=crypto_market)

game.start_new_game()
print(game.__dict__)