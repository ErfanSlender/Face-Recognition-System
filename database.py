import sqlite3

from datetime import datetime

from config import DATABASE_PATH


def create_database():
    
    conn = sqlite3.connect(DATABASE_PATH)
    
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        time TEXT NOT NULL
        
    )            
    """)
    
    conn.commit()
    conn.close()
    
def save_log(name):
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    
    current_time = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )
    
    cur.execute(
        "INSERT INTO logs (name, time) VALUES (?, ?)",
        (name, current_time)
    )
    
    conn.commit()
    conn.close()
    print(f"[DATABASE] {name} saved successfully!")
    
def get_all_logs():
    conn = sqlite3.connect(DATABASE_PATH)
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs ORDER BY id DESC")
    records = cur.fetchall()
    conn.close()
    return records