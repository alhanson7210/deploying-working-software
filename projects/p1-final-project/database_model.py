import sqlite3

class DatabaseComponent:
    def __init__(self, cursor):
        self.cursor = cursor

class DatabaseManager:
    def __init__(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        self.database = DatabaseComponent(cur)
