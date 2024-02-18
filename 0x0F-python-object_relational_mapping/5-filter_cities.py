#!/usr/bin/python3

"""
takes in the name of a state as an argument and lists all cities of that state
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    userName = argv[1]
    password = argv[2]
    db = argv[3]
    stateName = argv[4]

    conn = MySQLdb.connection(
            host="localhost",
            port=3306,
            user=userName,
            passwd=password,
            database=db
            )
    cur = conn.cursor()

    query = "SELECT city.name \
            FROM cities as city \
            JOIN states as st \
                ON city.state_id = st.id \
            WHERE st.name = '{stateName}' \
            ORDER BY city.id"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
