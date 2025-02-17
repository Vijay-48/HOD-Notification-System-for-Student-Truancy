# config/db_config.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, 'data', 'students.db')

# For simplicity, we are using SQLite. If you prefer MySQL, add your connection details.
DB_CONFIG = {
    'db_type': 'sqlite',  # Options: 'sqlite' or 'mysql'
    'sqlite_db_path': DATABASE_PATH,
}
