#!/usr/bin/python3
import MySQLdb
import sys

def main():
    """ Database connection parameters """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id"

    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        db.close()
        return

    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

