import sqlite3
from app.config import DB_PATH
from typing import List, Dict

# ✅ Initialize tables (users & conversations)
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                company TEXT,
                preferences TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                message TEXT,
                reply TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# ✅ Call it once to make sure DB is ready
init_db()

# ✅ Create user
def create_user(user) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            '''
            INSERT INTO users (name, email, company, preferences)
            VALUES (?, ?, ?, ?)
            ''',
            (user.name, user.email, user.company, user.preferences)
        )
        conn.commit()
        return c.lastrowid

# ✅ Update user
def update_user(user) -> bool:
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            '''
            UPDATE users SET
            name = COALESCE(?, name),
            email = COALESCE(?, email),
            company = COALESCE(?, company),
            preferences = COALESCE(?, preferences)
            WHERE id = ?
            ''',
            (user.name, user.email, user.company, user.preferences, user.user_id)
        )
        conn.commit()
        return c.rowcount > 0

# ✅ ✅ ✅ This is what you were missing:
def log_conversation(user_id: int, message: str, reply: str):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            '''
            INSERT INTO conversations (user_id, message, reply)
            VALUES (?, ?, ?)
            ''',
            (user_id, message, reply)
        )
        conn.commit()

# ✅ Get full chat history
def get_conversation_history(user_id: int) -> List[Dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(
            '''
            SELECT message, reply, timestamp FROM conversations
            WHERE user_id = ?
            ORDER BY timestamp ASC
            ''',
            (user_id,)
        )
        rows = c.fetchall()
        return [dict(row) for row in rows]
