#!/usr/bin/python3
"""MySQLdb script"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchName = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}'".format(matchName))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
