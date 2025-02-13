# utils/db_handler.py

import sqlite3
from config.db_config import DB_CONFIG

class DBHandler:
    def __init__(self):
        if DB_CONFIG['db_type'] == 'sqlite':
            self.conn = sqlite3.connect(DB_CONFIG['sqlite_db_path'], check_same_thread=False)
            self.create_tables()
        else:
            # Implement MySQL or other database connection if needed
            raise NotImplementedError("Only SQLite is implemented in this example.")

    def create_tables(self):
        cursor = self.conn.cursor()
        # Create table for students (if not exists)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                name TEXT,
                email TEXT,
                embedding BLOB
            )
        ''')
        # Create table for truancy logs
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS truancy_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                details TEXT
            )
        ''')
        self.conn.commit()

    def get_student(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
        return cursor.fetchone()

    def log_truancy(self, student_id, details):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO truancy_logs (student_id, details) VALUES (?, ?)', (student_id, details))
        self.conn.commit()
