#!/usr/bin/python3

"""
Lists all states from the states table of database hbtn_0e_0_usa.
Usage: ./0-select_states.py <username> \
                            <password> \
                             <database-name>
"""
import sys
import MySQLdb as db


def connect_query():

    """Connect to the database and execute query"""
    try:
        cnx = db.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id ASC;')
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_query()
