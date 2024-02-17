#!/usr/bin/python3

"""
Lists all states from the states table of database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""
import sys
import MySQLdb


def connect_query():

    """Connect to the database and execute query"""
    try:
        db = MySQLdb.connect(host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cur = db.cursor()
        rows = cur.execute('SELECT * FROM states ORDER BY states.id')

        for i in range(rows):
            print(cur.fetchone())
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_query()
