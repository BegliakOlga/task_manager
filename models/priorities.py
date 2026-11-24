from db import get_connection

def list_priorities() -> list[dict]:
    with get_connection() as connection:
        return connection.execute("SELECT id, name FROM priorities ORDER BY id").fetchall()