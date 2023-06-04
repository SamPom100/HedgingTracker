import os
import sqlite3

def init_database():
    if not os.path.isfile('../db/database.db'):
        os.system('touch ../db/database.db')
        with open('../db/database.db', 'r') as file:
            sqlite3.connect('../db/database.db', check_same_thread=False).cursor().execute(
            '''CREATE TABLE stocks (
                ticker TEXT,
                date TEXT,
                expirationDate TEXT,
                jsonData TEXT,
                UNIQUE(ticker, date, expirationDate)
            );
            '''
            )
            
class Database:

    def __init__(self):
        init_database()
        self.connection = sqlite3.connect('../db/database.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def execute(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def add_stock(self, ticker: str, date: str, expirationDate: str, jsonData: str):
        try:
            self.execute(f"INSERT INTO stocks VALUES ('{ticker}', '{date}', '{expirationDate}', '{jsonData}')")
        except:
            pass