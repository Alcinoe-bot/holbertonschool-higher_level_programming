#!/usr/bin/python3
"""
2-my_filter_states.py
"""
import MySQLdb
import sys


if __name__ == "__main__":
    "main"
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()
    state_name = sys.argv[4]
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC;").format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
