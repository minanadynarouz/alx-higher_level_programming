#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""

import sys
import MySQLdb as mydb


def connect_execute() -> None:

    """Connect to the database and execute query"""
    try:
        conn = mydb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                database=sys.argv[2]
                )
        cur = db .cursor(cursorclass=db.cursor.Cursor)
        cur.execute('SELECT * FROM states ORDER BY `id` ASC;')
        states = cur.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ = "__main__":
    connect_execute()
