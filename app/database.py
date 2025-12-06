import os
from contextlib import contextmanager

import psycopg2


def get_connection() -> psycopg2.extensions.connection:
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "mydb"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
        host=os.getenv("POSTGRES_HOST", "db"),
        port=os.getenv("POSTGRES_PORT", "5432")
    )


@contextmanager
def get_cursor():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
