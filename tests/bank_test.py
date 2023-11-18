import sys
import os

# Get the absolute path of the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the root directory to the Python path
sys.path.append(root_path)

from classes.finance.bank.bank import Bank
from classes.finance.cash.cash import Cash
from classes.finance.cash.cash_storage import CashStorage
from classes.finance.bank.bank_account import BankAccount
from classes.character.entity import Entity

cash = Cash('Test Cash')
bank_owner = Entity(name='Bank Owner')
bank = Bank(name='Test Bank', standard_cash=cash, owners=[bank_owner])
safe = CashStorage(name='Test Safe')

# add money to safe
safe.store(cash, 10000)

bank.deposit_cash(cash, 2400000)

# player and player account
account_holder = Entity(name='Account Holder')

# open bank account
account = bank.open_account(account_holder)

# deposit money
account.deposit(cash, 2000, safe)

# log balance
print('')
print('Deposit completed')
print('================================================')
print(f'Account balance: {account.get_balance()}')
print(f'Safe balance: {safe.contents[cash]}')
print(f'Vault balance: {bank.vault.contents[cash]}')

# withdraw money
account.withdraw(1000, safe, cash)

# log balance
print('')
print('Withdrawal completed')
print('================================================')
print(f'Account balance: {account.get_balance()}')
print(f'Safe balance: {safe.contents[cash]}')
print(f'Vault balance: {bank.vault.contents[cash]}')

# close bank account
bank.close_account(account, safe)

# log balance
print('')
print('Account closed')
print('================================================')
print(f'Account balance: {account.get_balance()}')
print(f'Safe balance: {safe.contents[cash]}')
print(f'Vault balance: {bank.vault.contents[cash]}')



