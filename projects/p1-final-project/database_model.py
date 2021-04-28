import sqlite3

class DatabaseComponent:
    def __init__(self, cursor):
        this.cursor = cursor

class DatabaseManager:
    def __init__(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        this.database = DatabaseComponent(cur)