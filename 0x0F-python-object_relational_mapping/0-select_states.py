#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""

import sys
import MySQLdb as mydb


def connect_execute():

    """Connect to the database and execute query"""
    try:
        db = mydb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                database=sys.argv[2]
                )
        cur = db.cursor()
        cur.execute('SELECT * FROM states ORDERBY `id` ASC;')
        states = cur.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ = "__main__":
    connect_execute()
