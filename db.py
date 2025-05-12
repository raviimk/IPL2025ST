import os
import sqlite3

DATABASE_URL = os.getenv("DATABASE_URL", "your_creat_xyz_connection_string_here")

def sql(query, params=()):
    with sqlite3.connect(DATABASE_URL) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, params)
        if query.strip().upper().startswith("SELECT") or "RETURNING" in query:
            return [dict(row) for row in cur.fetchall()]
        conn.commit()
        return []
