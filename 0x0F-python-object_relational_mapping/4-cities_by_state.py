#!/usr/bin/python3

"""
lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    userName = argv[0]
    password = argv[1]
    db = argv[2]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=userName,
            passwd=password,
            database=db
            )

    cur = conn.cursor()

    cur.execute(f"SELECT c.id, c.name, st.name \
        FROM cities AS c \
        JOIN states AS st \
            ON c.state_id = st.id \
        ORDER BY c.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
