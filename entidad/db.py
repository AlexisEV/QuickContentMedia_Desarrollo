
import psycopg2
from config import DB_CONFIG

_connection = None

def get_connection():
    global _connection
    if _connection is None or _connection.closed != 0:
        _connection = psycopg2.connect(**DB_CONFIG)
    return _connection