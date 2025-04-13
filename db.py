import sqlite3
from datetime import datetime

DB_NAME = "dice_rolls.db"

def initialize_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rolls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                die1 INTEGER NOT NULL,
                die2 INTEGER NOT NULL,
                total INTEGER NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()

def log_roll(die1: int, die2: int, total: int):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO rolls (die1, die2, total, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (die1, die2, total, timestamp))
        conn.commit()

def fetch_roll_history(limit: int = 10):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT die1, die2, total, timestamp
            FROM rolls
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()
