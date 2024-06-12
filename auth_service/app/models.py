import os
import sqlite3

def init_db():
    # Define o caminho do banco de dados dentro do diretório 'app'
    db_path = os.path.join(os.path.dirname(__file__), 'books.db') 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()
