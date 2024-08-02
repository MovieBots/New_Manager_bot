# database/database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('bot_database.db')
    return conn

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    # Create tables if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS premium_users (
                      user_id INTEGER PRIMARY KEY,
                      expiration_date TEXT)''')
    conn.commit()
    conn.close()

def add_premium_user(user_id, expiration_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO premium_users (user_id, expiration_date) VALUES (?, ?)',
                   (user_id, expiration_date.strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def remove_premium_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM premium_users WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

def get_premium_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM premium_users')
    users = cursor.fetchall()
    conn.close()
    return users
