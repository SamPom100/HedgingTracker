'''

Run this to add daily option data to the database

'''

from option import AutoStock

STOCK_LIST = [
    "AAPL",
    "NVDA",
    "SMCI",
    "AMD",
    "META",
    "TGLS"
]

for stock in STOCK_LIST:
    print("\nAdding", stock, "to database...")
    AutoStock(stock)