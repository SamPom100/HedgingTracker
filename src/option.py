# https://github.com/ranaroussi/yfinance
import yfinance as yf
import pandas as pd
from datetime import datetime
from tqdm import tqdm

from database import Database
DATABASE = Database()


class Stock:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ticker = yf.Ticker(name)
        self.option_expirations = self.ticker.options

    def add_to_database(self):
        today = datetime.today().strftime('%Y-%m-%d')
        if not DATABASE.fetch(f"SELECT * FROM stocks WHERE ticker='{self.name}' AND date='{today}'"):
            for date in tqdm(self.option_expirations):
                data = self.ticker.option_chain(date)
                data = data.calls.to_json()
                DATABASE.add_stock(self.name, today, date, data)
        
class AutoStock (Stock):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_to_database()