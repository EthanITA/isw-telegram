import json
import os

import psycopg2.extras

secrets = os.environ if os.environ.get('is_production') else json.load(open(os.path.join("secrets")))
conn = psycopg2.connect(
    database=secrets["db_name"],
    user=secrets["db_user"],
    password=secrets["db_password"],
    host='localhost',
    port='5432'
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def query_all(query: str, *args, **kwargs):
    cursor.execute(query, *args, **kwargs)
    return cursor.fetchall()
