import psycopg2
conn = psycopg2.connect("dbname=postgres user=marco password=isw.telegram")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
cur.execute("SELECT * FROM test;")
cur.fetchone()
conn.commit()
