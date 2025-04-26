import sqlite3
from tools.models import UserStats

DB_PATH = "user_data.db"

def init_db():
    """Initialize the SQLite database and create the necessary tables."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            height REAL,
            weight REAL,
            unit TEXT,
            activity TEXT,
            goal TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def save_user_stats(sender: str, stats: UserStats):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO user_stats (sender, age, height, weight, unit, activity, goal)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (sender, stats.age, stats.height, stats.weight, stats.unit, stats.activity, stats.goal))
    conn.commit()
    conn.close()
    

def get_user_stats(sender: str) -> UserStats:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT age, height, weight, unit, activity, goal FROM user_stats WHERE sender=?', (sender,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return UserStats(
            age=row[0],
            height=row[1],
            weight=row[2],
            unit=row[3],
            activity=row[4],
            goal=row[5]
        )
    return None